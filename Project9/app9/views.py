from django.shortcuts import render


def showIndex(request):
    return render(request,"index.html",{"name":"Ravi","Salary":185000})