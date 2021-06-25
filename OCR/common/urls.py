
from django.urls import path
from common import views

urlpatterns = [
    path('',views.showCommonPage,name='common_page')
]
