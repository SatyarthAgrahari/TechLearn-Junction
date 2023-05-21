from django.urls import path,include
from myapp  import  views 
urlpatterns = [
    path("",views.RegisterPage,name="registerpage"),
    path("register/",views.UserRegister,name="register"),
    path("loginPage/",views.LoginPage,name="loginpage"),
    path("loginUser/",views.LoginUser,name="loginuser"),
    path("home/",views.homepage,name="home"),
    path("about",views.aboutpage,name="about"),
]