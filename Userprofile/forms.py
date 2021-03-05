from django import forms

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'image',
            'full_name',
            'profession',
            'dept',
            'school',
            'phone',

        ]

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(UserProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(UserProfileForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst
