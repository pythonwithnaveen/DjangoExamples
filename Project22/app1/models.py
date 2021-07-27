from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AccountModel(models.Model):
    account_number = models.IntegerField(primary_key = True)
    employee = models.OneToOneField(EmployeeModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee.name