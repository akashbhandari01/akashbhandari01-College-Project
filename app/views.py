import datetime
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from django.contrib.auth import logout as user_logout, authenticate, login as user_login
from django.contrib.auth.models import User
from app.forms import *
from studybuddy.settings import *
from django.contrib import messages
from studybuddy import *
from .models import *
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'index.html')
def courses(request):
    return render(request,'courses.html')
def contact(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        universityroll=request.POST.get('universityroll')
        message=request.POST.get('message')
        data=Contact(fname=fname,lname=lname,email=email,universityroll=universityroll,message=message,date=datetime.today())
        data.save()
        messages.success(request,"Your massages has been successfully sent")
        data.save()
    return render(request,'contact.html')
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')
        if password1 != password2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')
        
        user=User.objects.create_user(username,email,password1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request, 'User created Successfully')
        return redirect('login')
    
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')       
        print(username, password)
        myuser = authenticate(username=username,password=password)
        print(username,password)
        if myuser is not None:
            user_login(request,myuser)
            
            return redirect('user/dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')
        
    return render(request,'login.html')
def logout(request):
    user_logout(request)
    messages.success(request,"Logout Successful")
    return redirect('login')
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def userdashboard(request):
    return render(request,'user/dashboard.html')

