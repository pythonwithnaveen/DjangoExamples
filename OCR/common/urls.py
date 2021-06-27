
from django.urls import path
from common import views

urlpatterns = [
    path('',views.showCommonPage,name='common_page'),
    path('student/',views.studentPage,name='student'),
    path('student_registration/',views.studentRegistration,name='student_registration'),

    path('student_otp/',views.openStudentOtp,name='student_otp')
]
