# Generated by Django 4.2.5 on 2023-09-22 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_customuser_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
