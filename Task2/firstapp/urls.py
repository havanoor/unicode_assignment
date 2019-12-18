from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns=[

    path('',auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('logouto/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('CreateUser/',user_views.CreateUser,name="create"),
    path('Register/',user_views.RegisterUser,name="created"),
    path('done/',user_views.update_value,name="updated"),
    path('home/',user_views.home,name="home"),
    path('withdraw/<str:value>/',user_views.withdraw,name="withdraw"),
    path('calc/<str:value>/',user_views.calc,name="cash"),
    path('profile/',user_views.update,name="update"),
    path('new/',user_views.register,name='new')
] 