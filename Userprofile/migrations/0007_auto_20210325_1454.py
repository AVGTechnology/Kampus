# Generated by Django 3.1.7 on 2021-03-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0006_remove_requestpayment_payment_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dept',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Dept.(Optional)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(default='full name', max_length=100, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='profession or skill'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='school',
            field=models.CharField(blank=True, default='Federal poly Auchi', max_length=100, null=True, verbose_name='School(Optional)'),
        ),
    ]
