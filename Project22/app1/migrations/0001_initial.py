# Generated by Django 3.1.4 on 2021-07-27 04:47

from django.db import migrations, models
import django.db.models.deletion


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
            ],
        ),
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('account_number', models.AutoField(primary_key=True, serialize=False)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.employeemodel')),
            ],
        ),
    ]