# Generated by Django 3.1.7 on 2021-04-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0008_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending',
            name='Trend_number',
            field=models.IntegerField(default=1),
        ),
    ]
