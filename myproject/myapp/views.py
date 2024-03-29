from django.shortcuts import redirect, render
from django.contrib.auth.models import *
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *

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
    queryset=receipt.objects.all()
    if req.method == "POST":
        iteam=req.POST.get("iteam")
        price=req.POST.get("price")
        quantity=req.POST.get("quantity")

        receipt.objects.create(
            itemname=iteam,
            price=price,
            quantity=quantity
        )
        queryset=receipt.objects.all()
        messages.info(req,"Item Added Succuessfully")
        return render(req,"billpage.html",context={"query":queryset})

    return render(req,"billpage.html",context={"query":queryset})


def delete(req,id):
    print(id)
    queryset=receipt.objects.all().get(id=id)
    queryset.delete()
    return redirect("/billpage")


def update(req,id):
    queryset=receipt.objects.get(id=id)
    context={"query":queryset}
    if req.method =="POST":
        
        item=req.POST.get("iteam")
        price=req.POST.get("price")
        quantity=req.POST.get("quantity")

        queryset.itemname=item
        queryset.price=price
        queryset.quantity=quantity
        queryset.save()

        return redirect("/billpage")

    return render(req,"update.html",context)