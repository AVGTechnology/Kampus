from django.db import models


# Create your models here.

class AboutApp(models.Model):
    title = models.TextField(max_length=225, verbose_name='Title', )
    about = models.TextField(max_length=5000, verbose_name='About', )
    image = models.ImageField(verbose_name='Image', upload_to='media/About_app/image')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'About {self.title}'


class AboutExcutives(models.Model):
    name = models.TextField(max_length=225, verbose_name='Name', )
    office = models.TextField(max_length=225, verbose_name='Office', )
    about = models.TextField(max_length=5000, verbose_name='About', )
    image = models.ImageField(verbose_name='Image', upload_to='media/About_Excutives/image')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'About {self.office}'
