from django.urls import path
from . import views

urlpatterns=[

    path('',views.logino,name="login"),
    path('check/',views.check,name="check"),
    path('logouto/',views.logouto,name="logout"),
    path('CreateUser/',views.CreateUser,name="create"),
    path('Register/',views.RegisterUser,name="created")
]