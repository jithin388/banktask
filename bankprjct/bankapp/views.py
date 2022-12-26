from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import details
from.models import place
from.models import Category
#from .forms import detailForm
# Create your views here.



def logon(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(detail)
        else:
            messages.info(request,"invalid user")
            return redirect(logon)
            
    
    return render (request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password'] 
        password1=request.POST['password1']
        if password== password1:
            if User.objects.filter(username=username).exists:
                messages.info(request,"username alredy exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists:
                messages.info(request,"email alredy exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                messages.info(request,"user created")
                
        else:
            messages.info(request,"password doesnot match") 
            return redirect(register)
        
        return redirect(logon)
    
    return render(request,'register.html')





def detail(request):
  
    if request.method=='POST':    
        username=request.POST['username']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        gender=request.POST['gender']
        dob=request.POST['dob']
        district=request.POST['district']
        branch=request.POST['branch']
        account=request.POST['account']
        
        material=request.POST.getlist('material')
        
        
        
        detail=details.objects.create(username=username,name=name,email=email,phone=phone,address=address,dob=dob,gender=gender,district=district,branch=branch,account=account,material=material)
        detail.save();
        messages.info(request,"sucessfully data stored")
        return redirect(details)
        
    
    return render(request,"details.html")


# def home(request,P_slug=None):
#     P_page = None
#     if P_slug !=None:
#         P_page = get_object_or_404(place,slug=P_slug)
        
#     return render (request, "home.html" ,{'plc':P_page,})

def home(request,c_slug=None):
    c_page=None
    
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        category=Category.objects.all().filter(category=c_page,available=True)
 
    return render(request,"home.html",{'category':c_page,})   
def places(request,P_slug=None):
    P_page=None
    if P_slug != None:
        P_page=get_object_or_404(place,slug=P_slug)
    return render(request,"navbar.html",{'plc':P_page,})
     
def logout(request):
    auth.logout(request)
    return redirect('/') 
