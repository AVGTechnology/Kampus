# Generated by Django 3.1.7 on 2021-03-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoneWithIt', '0002_auto_20210313_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='contact',
            field=models.BooleanField(default=False, verbose_name='Contact for price'),
        ),
        migrations.AlterField(
            model_name='item',
            name='free',
            field=models.BooleanField(default=False, verbose_name='Give item for free'),
        ),
    ]