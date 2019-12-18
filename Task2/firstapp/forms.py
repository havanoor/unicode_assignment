from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class new_user(UserCreationForm):
    email=forms.EmailField()
    Employee_id=forms.CharField()
    Department=forms.CharField()
    date_of_birth=forms.DateField()
    Gender=forms.CharField()


    class Meta:
        model=User
        fields=['username','Employee_id','Gender','email','Department','date_of_birth','password1','password2']