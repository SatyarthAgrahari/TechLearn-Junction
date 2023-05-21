from django.shortcuts import render
from myapp.models import MyUser
from datetime import datetime
# Create your views here.

#view for register page.
def RegisterPage(request):
    return render(request,"myapp/Register.html")

#view for user register
def UserRegister(request):
    if request.method =="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        # userlogin=UserLogin(Firstname='fname',Lastname='lname',Email='email',Contact='contact',Password='password', Date=datetime.today())
        # userlogin.save()

        #first we validate that user already exists.
        user=MyUser.objects.filter(Email=email).exists()
        if user:
            message="User Already Exists."
            return render(request,"myapp/Register.html",{'msg':message})
        else:
            if password==cpassword:
                userlogin=MyUser.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password, Date=datetime.today())
                userlogin.save()
                message="user register successfully."
                return render(request,"myapp/Login.html",{'msg':message})
            else:
                message="Password and confirm password does not match"
                return render(request,"myapp/Register.html",{'msg':message})


#view for user login
def LoginPage(request):
    return render(request,"myapp/Login.html")



def LoginUser(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        #checking the emailID with database.
        user=MyUser.objects.get(Email=email)

        if user:
            if user.Password==password:
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request,"myapp/home.html")
            else:
                message="Password does not match"
                return render(request,"myapp/Login.html",{'msg':message})
        else:
            message="User does not found! Please register with us"
            return render(request,"myapp/Register.html",{'msg':message})

# views for home page
def homepage(request):
    return render(request,"myapp/home.html")

#views for about page
def aboutpage(request):
    return render(request,"myapp/about.html")
        



    