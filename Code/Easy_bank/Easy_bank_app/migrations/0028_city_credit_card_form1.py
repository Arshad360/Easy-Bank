# Generated by Django 3.2 on 2021-08-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0027_brac_credit_card_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='city_credit_card_form1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicants_name', models.CharField(max_length=250)),
                ('applicants_full_name', models.CharField(max_length=200)),
                ('applicants_father_name', models.CharField(max_length=200)),
                ('applicants_mother_name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contatct_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('nid', models.CharField(max_length=100)),
                ('loan_type', models.CharField(max_length=200)),
            ],
        ),
    ]
