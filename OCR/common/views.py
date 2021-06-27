from django.shortcuts import render
from django.shortcuts import redirect
from student.models import RegistrationModel
from common.utils import sendTextMessage
from random import randint

def showCommonPage(request):
    return render(request,"common/index.html")


def studentPage(request):
    return render(request,"common/student.html")


def studentRegistration(request):
    if request.method == "POST":
        name = request.POST.get("student_name")
        contact = request.POST.get("student_contact")
        email = request.POST.get("student_email")
        password = request.POST.get("student_password")

        otp = randint(100000,999999)

        message = '''Thanks for Registration With Sathya, 
        To finish the Registration Use the Given OTP
        Your OTP : '''+str(otp)

        if sendTextMessage(message,contact):
            RegistrationModel(name=name,contact=contact,email=email,password=password,otp=otp).save()
        else:
            pass
        return redirect('student_otp')
    else:
        studentPage(request)


def openStudentOtp(request):
    return render(request,"common/otp.html")


