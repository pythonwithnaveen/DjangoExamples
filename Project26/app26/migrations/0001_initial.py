# Generated by Django 3.1.4 on 2021-08-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(choices=[('Developer', 'Developer'), ('Designaer', 'Designear'), ('Manager', 'Manager')], max_length=100)),
                ('contact', models.IntegerField()),
                ('photo', models.ImageField(upload_to='employee_images/')),
            ],
        ),
    ]