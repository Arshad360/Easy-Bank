# Generated by Django 3.0.5 on 2021-06-15 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0010_auto_20210603_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='phone',
        ),
    ]