from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='owner', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Profile Image', default='media/profile.jpg',
                              upload_to='media/profile_image',
                              null=True, blank=True)
    profession = models.CharField(max_length=20, verbose_name='profession or skill', null=True, blank=True)
    full_name = models.CharField(max_length=40, verbose_name="Full Name", default='full name', null=False, blank=False)
    dept = models.CharField(max_length=20, verbose_name="Dept.(Optional)", null=True, blank=True)
    school = models.CharField(max_length=20, verbose_name="School(Optional)", default="Federal poly Auchi", null=True,
                              blank=True)
    location = models.CharField(max_length=50, default=0, null=True, blank=True)
    phone = models.CharField(max_length=50, default='phone number', null=True, blank=True)
    join = models.DateTimeField(auto_now_add=True, editable=False)
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="mfollowed", blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="mfollowing", blank=True)

    def __str__(self):
        return f'{self.user} Profile '


class Relationship(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="follow", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.follower} followed {self.followed} '


class PaymentDetail(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='account', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, verbose_name='Account number', default='account number', null=False, blank=False)
    account_name = models.CharField(max_length=100, verbose_name='Account name', default='account name', null=False,
                                    blank=False)
    bank = models.CharField(max_length=30, verbose_name='Bank', default='bank', null=False, blank=False)
    paid = models.BigIntegerField(default=0)

    def __str__(self):
        return f'{self.user} '


class RequestPayment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='raccount', on_delete=models.CASCADE)
    Amount = models.BigIntegerField(default=0)
    paid = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} '
