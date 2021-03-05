from django.conf import settings
from django.db import models


# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="author", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='add image(optional)', upload_to='media/Article_Files',null=True, blank=True,)
    title = models.CharField(verbose_name='Title', max_length=225, null=False, blank=False, )
    body = models.TextField(verbose_name='Body', max_length=1500, null=False, blank=False, )
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    views = models.BigIntegerField(default=0, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.title} Article '


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="user_article", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name="article_com", on_delete=models.CASCADE)
    comment = models.CharField(max_length=225, verbose_name='comment', default='write a comments...')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.article} '
