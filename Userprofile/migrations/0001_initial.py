# Generated by Django 3.1.7 on 2021-02-25 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='media/profile.jpg', null=True, upload_to='media/profile_image', verbose_name='Profile Image')),
                ('profession', models.CharField(blank=True, max_length=20, null=True, verbose_name='profession or skill')),
                ('full_name', models.CharField(default='full name', max_length=40, verbose_name='Full Name')),
                ('dept', models.CharField(blank=True, max_length=20, null=True, verbose_name='Dept.(Optional)')),
                ('school', models.CharField(blank=True, default='Federal poly Auchi', max_length=20, null=True, verbose_name='School(Optional)')),
                ('location', models.CharField(blank=True, default=0, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, default='phone number', max_length=50, null=True)),
                ('join', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
