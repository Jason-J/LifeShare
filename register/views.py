from django.shortcuts import render
# coding:utf-8
# Create your views here.
from django.http import HttpResponse
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
# def login(req):
#     if req.method == 'POST':
#     return 0

def login(request):
    user = UserForm()
    if request.method == "POST":
        print(request.POST)
        userInputInfo = UserForm(request.POST)
        print(userInputInfo)
        index(request)
    return render(request,'login.html',{'userinfo':user})

def index(request):
    userLogin = request.POST
    return render(request,'index.html',{'userLogin':userLogin})
def register(request):
    return render(request,'register.html')