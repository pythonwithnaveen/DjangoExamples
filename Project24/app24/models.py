from django.db import models


class EmployeeModel(models.Model):

    desig = (('Manager','Manager'),
             ('Developer','Developer'),
             ('Tester','Tester'))

    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    designation = models.CharField(max_length=100,choices=desig,default='Developer')


    def __str__(self):
        return self.name