# Generated by Django 4.2.2 on 2023-07-05 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_profileimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profileimage',
        ),
    ]
