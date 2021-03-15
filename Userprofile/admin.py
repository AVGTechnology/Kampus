from django.contrib import admin
from .models import UserProfile, Relationship, PaymentDetail, RequestPayment


# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "profession", "full_name", "dept", "school", "phone", "location", "join", "image",)


admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Relationship)

admin.site.register(PaymentDetail)

admin.site.register(RequestPayment)