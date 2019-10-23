from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout


# Create your views here.


def logino(request):  
    
    return render(request,"login.html")


def check(request):
     Uname=request.GET['login']
     Pword=request.GET['password']
     res=authenticate(username=Uname,password=Pword)
     

     if res:
         login(request,res)
         return render(request,"logout.html")

     else:
         return render(request,"login.html",{'message':"Try Again"})

def logouto(request):
    logout(request)

    return render(request,"login.html",{'message':"Logged out"})



     