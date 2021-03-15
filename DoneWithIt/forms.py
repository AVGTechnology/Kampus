from django import forms

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'first_image',
            'item_name',
            'category',
            'item_dis',
            'location',
            'contact',
            'price',
            'free',
            'negotiable',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(ItemForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(ItemForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


