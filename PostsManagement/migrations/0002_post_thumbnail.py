# Generated by Django 3.1.7 on 2021-04-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostsManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default="'static/images/logo.png'", upload_to='media/Post_thumbnail'),
        ),
    ]