# Generated by Django 3.1.4 on 2021-06-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registrationmodel',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
