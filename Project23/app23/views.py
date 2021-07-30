from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request, "index.html")


    # if request.method == "POST":
    #     return render(request,"index.html")
    # if request.method == "GET":
    #     return HttpResponse("I am Get")


def save(request):
    if request.method == "POST":
        return HttpResponse("OK")
    else:
        return HttpResponse("Thanks")