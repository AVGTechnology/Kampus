from django.conf import settings
from django.db import models

# Create your models here.

Item_Category = (
    ("Book", "Book"),
    ("Phone", "Phone"),
    ("Computer", "Computer"),
    ("Appliances", "Appliances"),
    ("Gadget", "Gadget"),
    ("Furniture", "Furniture"),
    ("Apartment", "Apartment"),
    ("Clothing", "Clothing"),
    ("Vehicle", "Vehicle"),
    ("Kitchen", "Kitchen"),
    ("Others", "Others"),
)


class Item(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="item_owner", on_delete=models.CASCADE)
    first_image = models.FileField(verbose_name='Image', upload_to='media/Donewithit', null=False, blank=False, )
    item_name = models.CharField(verbose_name='Item Name', max_length=100, null=False, blank=False, )
    item_dis = models.TextField(verbose_name='Description', max_length=225, null=True, blank=True, )
    category = models.CharField(max_length=150, choices=Item_Category, default="Book")
    location = models.CharField(verbose_name='location', max_length=225, null=True, blank=True, )
    price = models.IntegerField(default=0, verbose_name='Price', null=True, blank=True, )
    sold = models.BooleanField(default=False)
    free = models.BooleanField(default=False, verbose_name='Give item for free', )
    negotiable = models.BooleanField(default=True, verbose_name='Negotiable',)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} sell {self.item_name}  '
