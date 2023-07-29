from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('courses',views.courses,name='courses'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('user/dashboard',views.userdashboard,name='userdashboard'),
    path('user/logout',views.logout,name='logout'),
]