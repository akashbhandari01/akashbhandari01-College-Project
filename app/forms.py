from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from .models import *
from django.forms import inlineformset_factory

class registerform(UserCreationForm):
    username=forms.IntegerField()
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)

    class meta:
        model = User
        fields = ('username', 'fname','lname', 'email','password1','password2')
    def save(self, commit=True):
        User = super(registerform,self).save(commit=False)
        User.email=self.cleaned_data['email']
        User.fname=self.cleaned_data['fname']
        User.lname=self.cleaned_data['lname']
        User.password1=self.cleaned_data['password1']
        User.password2=self.cleaned_data['password2']
        if commit:
            User.save()
        return User

# class loginform(UserLoginForm):
#     unsername=forms.IntegerField()
    
#     class meta:
#         model=User
#         fields=['username', 'password']
    