from django import forms

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'file',
            'caption',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(PostForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment',

        ]


class ThumbnailForm(forms.ModelForm):
    class Meta:
        model = Post_thumbnail
        fields = [
            'thumbnail',

        ]
