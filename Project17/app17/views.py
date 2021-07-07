from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html",)


def saveStudent(request):
    if request.method == "POST":
        name = request.POST.get("name")
        cno = request.POST.get("contact")
        photo = request.FILES['photo']
        dob = request.POST.get('DOB')
        email = request.POST.get("email")
        password = request.POST.get("password")


