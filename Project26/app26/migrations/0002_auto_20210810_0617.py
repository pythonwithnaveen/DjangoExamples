# Generated by Django 3.1.4 on 2021-08-10 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app26', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='contact',
            field=models.IntegerField(unique=True),
        ),
    ]
