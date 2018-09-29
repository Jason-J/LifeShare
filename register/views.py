from django.shortcuts import render
# coding:utf-8
# Create your views here.
from django.http import HttpResponse
from django import forms
from register.models import Person as User
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
    registForm = UserForm(request.POST)
    if registForm.is_valid():
        rgUsername = registForm.cleaned_data['username']
        rgPassword = registForm.cleaned_data['password']
        registAdd = User.objects.create(name=rgUsername, userpassword=rgPassword)
        if registAdd == False:
            return render(request,'register.html',{'registerAdd':registAdd, 'username':rgUsername})
        else:
            return render(request,'index.html.html',{"registerAdd":registAdd})

    return render(request,'register.html',{'registForm':registForm})