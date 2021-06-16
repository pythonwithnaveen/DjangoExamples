from django.shortcuts import render


# Create your views here.
def showMainPage(request):
    return render(request,"main.html")


def showRegisterPage(request):
    return render(request,"register.html")


def showLoginPage(request):
    return render(request,"login.html")