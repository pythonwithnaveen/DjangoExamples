from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

from app26.models import EmployeeModel


# class ShowIndex(TemplateView):
#     template_name = 'index.html'



class AddEmployee(CreateView):
    template_name = 'add_employee.html'
    model = EmployeeModel
    fields = "__all__"
    success_url = '/view_all_employees/'


class ViewAllEmployees(ListView):
    template_name = 'view_all_employee.html'
    model = EmployeeModel
    queryset = EmployeeModel.objects.values('idno','name','contact')


class ViewOneEmployee(DetailView):
    template_name = 'view_one_employee.html'
    model = EmployeeModel


class UpdateEmployee(UpdateView):
    template_name = 'update_employee.html'
    model = EmployeeModel
    fields = "__all__"
    success_url = '/view_all_employees/'


class DeleteEmployee(DeleteView):
    template_name = 'delete_employee.html'
    model = EmployeeModel
    success_url = '/view_all_employees/'