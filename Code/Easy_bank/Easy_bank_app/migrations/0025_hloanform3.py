# Generated by Django 3.2.2 on 2021-08-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0024_auto_20210828_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='hloanform3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(max_length=100)),
                ('floor_size', models.CharField(max_length=100)),
                ('flat_no', models.CharField(max_length=100)),
                ('nationality_2', models.CharField(max_length=100)),
                ('utility', models.CharField(max_length=100)),
                ('expected_possesion', models.CharField(max_length=100)),
                ('date_expected', models.CharField(max_length=100)),
            ],
        ),
    ]
