from django.contrib import admin
from .models import *

admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "post", "timestamp",)


admin.site.register(Comment, CommentAdmin)
