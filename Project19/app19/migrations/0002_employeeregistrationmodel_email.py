# Generated by Django 3.1.4 on 2021-07-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app19', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeregistrationmodel',
            name='email',
            field=models.EmailField(default='sathya@gmail.com', max_length=100),
        ),
    ]
