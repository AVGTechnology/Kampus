# Generated by Django 3.1.7 on 2021-02-28 22:15

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/Article_Files', verbose_name='add image(optional)')),
                ('title', models.CharField(max_length=225, verbose_name='Title')),
                ('body', models.TextField(max_length=1500, verbose_name='Body')),
                ('views', models.BigIntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('like', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='write a comments...', max_length=225, verbose_name='comment')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_com', to='StudentGuildian.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_article', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
