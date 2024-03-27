from django.shortcuts import redirect, render
from django.contrib.auth.models import *
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def home(req):
    return render(req,'home.html')


def signup(req):
    if req.method == "POST":
        username=req.POST.get('username')
        email=req.POST.get('email')
        password=req.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(req,"User Already Exists")
        else:
            user=User.objects.create_user(
                username=username,
                email=email

            )
            user.set_password(password)
            user.save()
            messages.info(req,"Account created Successfully")

    return render(req,"signup.html")

def login(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(req,"User Doesn't exits")
        else:
            user=authenticate(username=username,password=password)
            if user is None:
                messages.info(req,"Invalid Password")
            else:
                return redirect("/billpage")
    return render(req,"login.html")

def billpage(req):
    return render(req,"billpage.html")