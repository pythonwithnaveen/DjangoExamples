"""Project26 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Project26 import settings
from app26 import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('',views.ShowIndex.as_view(),name='main'),
    #  ---- or ----
    path('',views.TemplateView.as_view(template_name='index.html'),name='main'),


    path('add_employee/',views.AddEmployee.as_view(),name='add_employee'),
    path('view_all_employees/',views.ViewAllEmployees.as_view(),name='view_all_employees'),

    path('view_one/',TemplateView.as_view(template_name="view_one.html"),name='view_one'),

    path('view_one_employee/<int:pk>/',views.ViewOneEmployee.as_view(),name='view_one_employee'),

    path('update_employee/<int:pk>/',views.UpdateEmployee.as_view(),name='update_employee'),

    path('delete_employee/<int:pk>/',views.DeleteEmployee.as_view(),name='delete_employee'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

