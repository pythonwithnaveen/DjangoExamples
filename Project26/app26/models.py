from django.db import models



class EmployeeModel(models.Model):
    designantion_choices = (('Developer','Developer'),
                            ('Designaer','Designear'),
                            ('Manager','Manager'))

    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(choices=designantion_choices,max_length=100)
    contact = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='employee_images/')
