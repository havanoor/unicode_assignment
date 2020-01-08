from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from . import models
from django.shortcuts import redirect
from django.urls import reverse
from .forms import new_user




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
    return HttpResponseRedirect(reverse("home"))

def home(request):

   # k=value1.split(',')
    t=request.user.username
    print(t)

    
    current_user=models.Employee.objects.filter(users=User.objects.filter(username=t).first()).first()
    print(current_user)

    job=models.Jobs.objects.filter(employee=current_user)
    amount=models.MonthlyExpense.objects.filter(employee=current_user)
    owner=models.Balance.objects.filter(employee=current_user).first()
    print(owner.Balance)

    message="You have sufficient balance"

    if owner.Balance <1000:
        
        message="You have less balance!!"

    val={'job':job,'owner':owner,'username':t,'message':message,'amount':amount,'id':current_user.Employee_id}

    return render(request,"home.html",val)
    
    
    #return HttpResponse(request.user.username)


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
    return HttpResponseRedirect(reverse("home" ))


def update(request):
    
     #empl=models.Employee.objects.filter(Employee_id=request.POST['code3'])
    #print(empl)
    #job=models.Jobs.objects.filter(employee=empl[0])
    user=models.Employee.objects.filter(Employee_id=request.POST['code3'])

    
    
    print(user[0])
    #print(job)
    
    if 'add' in request.POST:
        newjob=models.Jobs()
        newjob.Income=request.POST['income']
        newjob.JobName=request.POST['jobname']
        newjob.Increment=request.POST['increment']
        newjob.employee=user[0]
        newjob.save()
    elif 'withdraw' in request.POST:
        job=models.Jobs.objects.filter(employee=user[0])
        job.delete()
        #job.save()

    return HttpResponseRedirect(reverse("home"))



def register(request):
    form=new_user(request.POST)
    if form.is_valid():
        emp=models.Employee()
        bal=models.Balance()
        form.save()
        t=form.cleaned_data['username']
        print(t)
        print(User.objects.filter(username=t).first())
        emp.users=User.objects.filter(username=t).first()
        #print(emp.users)
        
        emp.Employee_id=request.POST['Employee_id']
        emp.Gender=request.POST['Gender']
        emp.Department=request.POST['Department']
        emp.Date_of_Birth=request.POST['date_of_birth']
        bal.Balance=0
        bal.users=User.objects.filter(username=t).first()
        bal.employee=emp
        emp.save()
        bal.save()
        
        return redirect('login')

    else :
        form=new_user()

    return render(request,'NewUser.html',{'form':form})





        

 







    
    




