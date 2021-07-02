# Generated by Django 3.1.4 on 2021-06-27 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210627_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='contact',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='registrationmodel',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]