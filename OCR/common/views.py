from django.shortcuts import render

# Create your views here.
def showCommonPage(request):
    return render(request,"common/index.html")