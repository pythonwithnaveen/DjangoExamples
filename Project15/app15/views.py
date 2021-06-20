from django.shortcuts import render
from django.http import HttpResponse
from app15.models import Registration


# Create your views here.
def showMainPage(request):
    return render(request,"main.html")


def showRegisterPage(request):
    if request.method == "POST":
        n = request.POST.get("name")
        con = request.POST.get("contact")
        loc = request.POST.get("location")
        email = request.POST.get("email")
        password = request.POST.get("password")

        Registration(name=n,contact=con,location=loc,email=email,password=password).save()

        return render(request,"register.html",{"message":"Registration is Done"})

    else:
        return render(request,"register.html")


def showLoginPage(request):
    return render(request,"login.html")