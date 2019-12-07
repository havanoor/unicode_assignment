from django.urls import path
from . import views

urlpatterns=[

    path('',views.logino,name="login"),
    path('check/',views.check,name="check"),
    path('logouto/',views.logouto,name="logout"),
    path('CreateUser/',views.CreateUser,name="create"),
    path('Register/',views.RegisterUser,name="created"),
    path('done/',views.update_value,name="updated"),
    path('home/<str:value1>/',views.home,name="home"),
    path('withdraw/<str:value>/',views.withdraw,name="withdraw"),
    path('calc/<str:value>/',views.calc,name="cash"),
    path('profile/',views.update,name="update")
] 