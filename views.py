from django.shortcuts import render
from .models import UserDetails
# Create your views here.
def home(req):
    return render(req,"main-home.html")

def about(req):
    return render(req,"about.html")

def register(req):
    if req.method=="POST":
        username = req.POST.get("uname")
        email = req.POST.get("email")
        password = req.POST.get("pwd")
        dob = req.POST.get("dob")

        print(username,email,password,dob)

        details = UserDetails(uname=username,
                              email=email,
                              password=password,
                              dob=dob)
        
        details.save()


    return render(req,"register.html")

def login(req):
    return render(req,"login.html")