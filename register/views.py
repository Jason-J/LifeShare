from django.shortcuts import render
# coding:utf-8
# Create your views here.
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
# def login(req):
#     if req.method == 'POST':
#     return 0

def login(request):
    userForm = UserForm()
    if request.method == "POST":

        loginForm = UserForm(request.POST)
        username = loginForm['username']
        password = loginForm['password']
        re = auth.authenticate(username=username,password=password)
        if re is not None:
            auth.login(request,re)
            print('login successs!!!!')
            return render(request,'index.html',{'userLogin':username})
        else:
            return render(request, 'login.html',{'Login_error':'用户名或密码错误','userinfo':userForm})
    return render(request,'login.html',{'userinfo':userForm})

def index(request):
    userLogin = request.POST
    return render(request,'index.html',{'userLogin':userLogin})
def register(request):
    registForm = UserForm(request.POST)
    if registForm.is_valid():
        rgUsername = registForm.cleaned_data['username']
        rgPassword = registForm.cleaned_data['password']
        print(rgUsername,rgUsername)
        registAdd = User.objects.create(username=rgUsername, password=rgPassword)
        if registAdd == False:
            return render(request,'register.html',{'registerAdd':registAdd, 'username':rgUsername})
        else:
            return render(request,'index.html',{"registerAdd":registAdd})

    return render(request,'register.html',{'registForm':registForm})