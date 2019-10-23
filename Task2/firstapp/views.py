from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.


def logino(request):  
    
    return render(request,"login.html")


def check(request):
     Uname=request.POST['login']
     Pword=request.POST['password']
     res=authenticate(username=Uname,password=Pword)
     

     if res:
         login(request,res)
         return render(request,"logout.html")

     else:
         return render(request,"login.html",{'message':"Try Again"})

def logouto(request):
    logout(request)

    return render(request,"login.html",{'message':"Logged out"})

def CreateUser(request):

    return render(request,"NewUser.html")

def RegisterUser(request):
    u=request.POST['user']
    p=request.POST['password']
    e=request.POST['email']
    user = User.objects.create_user(u,e,p)
    user.save()

    return HttpResponse("User created")



     