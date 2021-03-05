from django import forms

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = [
            'text',
        ]
