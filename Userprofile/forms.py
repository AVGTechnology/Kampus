from django import forms
from django.forms import ModelForm

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentDetail
        fields = [
            'account_number',
            'account_name',
            'bank',

        ]


class PayrequstForm(forms.ModelForm):
    class Meta:
        model = RequestPayment
        fields = [
            'user',
            'Amount',
            'pending',

        ]


class PaymentEditForm(ModelForm):
    class Meta:
        model = PaymentDetail
        fields = [
            'account_number',
            'account_name',
            'bank',

        ]


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


class ImageEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)
