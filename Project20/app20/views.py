from django.shortcuts import render,redirect
from app20.forms import StudentForm
from app20.forms import CourseForm
from app20.models import StudentModel
from app20.models import CourseModel

# Create your views here.
def showIndex(request):
    course = CourseForm(request.POST)
    if request.method == "POST":
        course.save()
        return redirect('main')
    else:
        return render(request,"index.html",{"c_form":course,"all_courses":CourseModel.objects.all()})


def showStudent(request):
    student = StudentForm(request.POST)
    if request.method == "POST":
        student.save()
        return redirect('student')
    else:
        result = CourseModel.objects.all()
        if result:
            return render(request, "studnet.html", {"s_form": StudentForm(),"all_students":StudentModel.objects.all()})
        else:
            return render(request, "studnet.html", {"error": "Please Add Course"})



def foo():
    all_students = StudentModel.objects.all()
    for student in all_students:
        all_course = student.course.all()
        for course in all_course:
            course.course_fee