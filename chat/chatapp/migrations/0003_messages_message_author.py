# Generated by Django 4.2.2 on 2023-07-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_remove_messages_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message_author',
            field=models.CharField(default=True, max_length=100),
        ),
    ]