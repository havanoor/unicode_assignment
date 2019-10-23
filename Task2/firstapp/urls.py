from django.urls import path
from . import views

urlpatterns=[

    path('',views.logino,name="login"),
    path('check/',views.check,name="check"),
    path('logouto/',views.logouto,name="logout"),
]