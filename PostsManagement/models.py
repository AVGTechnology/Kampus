from django.conf import settings
from django.db import models


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="user_video_post", on_delete=models.CASCADE)
    file = models.FileField(verbose_name='Post', upload_to='media/Post_Files')
    caption = models.CharField(verbose_name='Write a caption..', max_length=1500, null=True, blank=True, )
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    dislike = models.BigIntegerField(default=0, null=True, blank=True, )
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} Post '

    def __unicode__(self):
        return self.file

    def find_typecheck(self):
        filename = self.file.name
        try:
            ext = filename.split('.')[-1]
            if ext == 'jpg':
                a = 1

            elif ext == 'jpeg':
                a = 1

            elif ext == 'png':
                a = 1

            elif ext == 'gif':
                a = 1

            elif ext == 'mp4':
                a = 2

            elif ext == 'avi':
                a = 2

            elif ext == 'mov':
                a = 2

            elif ext == 'mkv':
                a = 2

            else:
                a = 3
        except Exception:
            a = -1  # couldn't determine
        return a


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="commenter", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_com", on_delete=models.CASCADE)
    comment = models.CharField(max_length=225, verbose_name='comment', default='write a comments...')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.post} Post '


class Post_thumbnail(models.Model):
    thumbnail = models.ImageField(verbose_name='Post Thumbnail', upload_to='media/Post_thumbnail', blank=True, null=True)

    def __str__(self):
        return f'image {self.thumbnail}'
