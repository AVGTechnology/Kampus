# Generated by Django 3.1.7 on 2021-04-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0007_auto_20210325_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.BigIntegerField(default=0)),
                ('likes', models.BigIntegerField(default=0)),
            ],
        ),
    ]
