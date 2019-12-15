from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employee(models.Model):
    users=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    Employee_id=models.CharField(primary_key=True,blank=False,max_length=30)
    Department=models.CharField(blank=False,max_length=30)
    Email=models.EmailField(blank=False,max_length=30)
    Date_of_Birth=models.DateField()
    Gender=models.CharField(blank=False,max_length=10)
    Postion=models.CharField(blank=False,max_length=30)





class MonthlySaving(models.Model):
    Month=models.DateField()
    TotalSaved=models.IntegerField(blank=False) 
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)

    
class MonthlyExpense(models.Model):
    Month=models.DateField()
    TotalAmount=models.IntegerField(blank=False)
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)

class YearlySaving(models.Model):
    Year=models.DateField()
    TotalAmount=models.IntegerField(blank=False)
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)
    YearlyDifference=models.IntegerField(blank=False)


class YearlyExpenditure(models.Model):
    Year=models.DateField()
    TotalAmount=models.IntegerField(blank=False)
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)
    YearlyDifference=models.IntegerField()


class Jobs(models.Model):
    JobName=models.CharField(blank=True,max_length=40)
    Income=models.IntegerField()
    Increment=models.IntegerField()
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)
   
class Balance(models.Model):
    Balance=models.IntegerField(blank=False)
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)



