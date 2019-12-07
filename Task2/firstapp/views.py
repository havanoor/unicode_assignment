from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from . import models
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.


def logino(request):  
    
    return render(request,"login.html")


def check(request):
     Uname=request.POST['login']
     Pword=request.POST['password']
     Empcode=request.POST['emp']
     res=authenticate(request,username=Uname,password=Pword)

     

     if res:       
         
         

         val={'username':Uname,'code':Empcode}
         login(request,res)
         return render(request,"logout.html",val)

     else:
         return render(request,"login.html",{'message':"Try Again"})

def logouto(request):
    logout(request)

    #return render(request,"login.html",{'message':"Logged out"})
    return redirect('login')

def CreateUser(request):

    return render(request,"NewUser.html")

def RegisterUser(request):
    #attributes of a user from the html page
    uname=request.POST['user']
    pword=request.POST['password']
    email=request.POST['email']
    empcode=request.POST['code']
    dob=request.POST['date']
    pos=request.POST['pos']
    gender=request.POST['gender']
    dep=request.POST['dep']
    
    emp=models.Employee()
    emp.Date_of_Birth=dob
    emp.Email=email
    emp.Employee_id=empcode
    emp.Gender=gender
    emp.Postion=pos
    emp.Department=dep

    #saving our created users
    emp.save()
    user = User.objects.create_user(uname,email,pword)
    user.save()

    #initial balance is 0
    bal=models.Balance()
    bal.Balance=0
    bal.employee=emp
    bal.save()

 
    return HttpResponse("User created")


def update_value(request):
    
    
    expense=models.MonthlyExpense()
    expense.Month=request.POST['month']
    expense.TotalAmount=int(request.POST['amount'])      
    employee=request.POST['code']
    test=models.Employee.objects.filter(Employee_id=employee)
    expense.employee=test[0]
    expense.save()

    job=models.Jobs.objects.filter(employee=expense.employee)
    salary=0
    for jo in job:
        salary=salary+jo.Income
    saving=models.MonthlySaving()
    saving.Month=request.POST['month']
    saving.employee=test[0]
    saving.TotalSaved=salary-expense.TotalAmount
    saving.save()

    temp=models.Balance.objects.filter(employee=expense.employee)
    balance=temp[0]

    balance.Balance += saving.TotalSaved

    balance.save()
    


    
 #   return render(request,'logout.html')
    #return redirect('home')
    return HttpResponseRedirect(reverse("home" ,kwargs={'value1':employee}))

def home(request,value1):
   # k=value1.split(',')
    user=models.Employee.objects.filter(Employee_id=value1)

    job=models.Jobs.objects.filter(employee=user[0])
    amount=models.MonthlyExpense.objects.filter(employee=user[0])
    owner=models.Balance.objects.filter(employee=user[0])
    message="You have sufficient balance"

    if owner[0].Balance <1000:
        message="You have less balance!!"

    val={'job':job,'owner':owner,'username':value1,'message':message,'amount':amount}

    return render(request,"home.html",val)


def withdraw(request,value):
    if value=='withdraw':
        return render(request,'withdraw.html',{'val':'withdraw'})

    elif value=='expense':
        return render(request,"Update.html")
    elif value=='add':
        return render(request,"withdraw.html",{'val':'add'})
    elif value=='update':
        return render(request,"job.html",{'status':'update'})


def calc(request,value):
    employee=request.POST['code2']
    test=models.Employee.objects.filter(Employee_id=employee)
    test2=models.Balance.objects.filter(employee=test[0])
    balance=test2[0]
    if value=='withdraw':
        balance.Balance -=int(request.POST['val'] )
    elif value=='add':
        balance.Balance +=int(request.POST['val'] )

    

    
    
    balance.save()


    #return reverse("home" ,kwargs={'value1':employee})
    return HttpResponseRedirect(reverse("home" ,kwargs={'value1':employee}))


def update(request):
    
     #empl=models.Employee.objects.filter(Employee_id=request.POST['code3'])
    #print(empl)
    #job=models.Jobs.objects.filter(employee=empl[0])
    user=models.Employee.objects.filter(Employee_id=request.POST['code3'])

    
    
    print(user[0])
    #print(job)
    
    if 'Add' in request.POST:
        newjob=models.Jobs()
        newjob.Income=request.POST['income']
        newjob.JobName=request.POST['jobname']
        newjob.Increment=request.POST['increment']
        newjob.employee=user[0]
        newjob.save()
    elif 'Remove' in request.POST:
        job=models.Jobs.objects.filter(employee=user[0])
        job.delete()
        #job.save()

    return HttpResponseRedirect(reverse("home" ,kwargs={'value1':request.POST['code3']}))
        

 







    
    




