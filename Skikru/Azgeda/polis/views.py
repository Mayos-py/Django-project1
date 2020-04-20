from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.forms import forms
from .models import Register

# Create your views here.
def index(request):
    return render(request,'index.html')


def check(request):
    if request.method == 'POST':
        name1= request.POST['name']
        phone= request.POST['phone']
        email= request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd == cpwd:
            register = Register(name=name1, phone=phone, email=email, password=pwd)
            print('success')
            register.save()

            return render(request, 'dashboard.html')
        else:
            raise forms.ValidationError("Password not matching")
    else:
        return render(request,'index.html')

def dashboard(request):
    if request.method == 'POST':
        x = request.POST['email1']
        y = request.POST['pwd1']
        # print(x, y)

    obj1 = Register.objects.filter(email__startswith=x).values('password')
    new = obj1[0]['password']

    if new == y:

        obj2 = Register.objects.filter(email__startswith=x).values('name')
        new1 = obj2[0]['name']
        obj4 = Register.objects.filter(email__startswith=x).values('phone')
        new3 = obj4[0]['phone']

        return render(request, "other.html",{'name': new1,'email': x, 'phone': new3})
    else:

        return render(request, "dashboard.html",{'data': new })

def login(request):
    return render(request, "dashboard.html")



