from django.contrib import admin
from app24.models import EmployeeModel
from django.contrib.auth.models import Group,User


#admin.site.register(EmployeeModel)

admin.site.unregister(User)
admin.site.unregister(Group)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['idno','name','salary','designation']
    list_filter = ['salary','designation']



admin.site.register(EmployeeModel,EmployeeAdmin)

admin.site.site_title = "Sathya Tech"
admin.site.site_header = "Django Admin Login"