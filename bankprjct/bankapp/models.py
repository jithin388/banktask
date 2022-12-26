from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=30,unique=True)
    slug=models.SlugField(max_length=30,unique=True)
    
class details(models.Model):
    ACCOUNT_CHOICES=(("S","savings"),("C","current"))
    MATERIAL_CHOICES=(("d","debitcard"),("c","creditcard"),("p","prepaidcard"),("q","cheque"))
    boolChoice=(("M","male"),("F","female"),("O","other"))
    username=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length=30,unique=True)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    gender=models.CharField(max_length=30,choices=boolChoice)
    address=models.CharField(max_length=30)
    dob=models.DateField(max_length=30)
    district=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    account=models.CharField(max_length=30,choices=ACCOUNT_CHOICES)
    material=models.CharField(max_length=200,)

    class Meta:
        ordering=('name',)
        verbose_name='detail'
        verbose_name_plural='details'
    def __str__(self):
        return self.name
     
     
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    images=models.ImageField(upload_to='category',blank=True)