# Generated by Django 3.2.2 on 2021-08-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0016_homeloanappform'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeloanappform',
            name='additional_income',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='allowness',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='balance_amount',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='contact_2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='date_expected',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='designation_department',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='email_3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='expected_possesion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='flat_no',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='floor_size',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='full_address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='home_area',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='loan_requested',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='nationality_2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='office_address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='office_no',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='organisation_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='p_address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='payment_source',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='postal_code',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='property_selected',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='property_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='salary_total',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='second_contact_no',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='second_email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeloanappform',
            name='utility',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
