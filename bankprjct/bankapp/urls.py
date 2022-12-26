
from django.urls import path
from . import views
urlpatterns = [
    path('logon',views.logon,name='logon'),
    path('detail',views.detail,name='detail'),
    path('register',views.register,name='register'),
    
    path('places',views.places,name='places'),
    path('logout',views.logout,name='logout'),
    path('',views.home,name='home'),
    
    
]
