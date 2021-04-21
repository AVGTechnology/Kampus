from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static
from DoneWithIt.views import Item

urlpatterns = [

    #path('donewithit/', views.items, name='donewithit'),
    path('donewithit/', Item.as_view(),  name="donewithit"),
    path('sell/item/', views.sell_item, name='sell_item'),
    path('account/', views.account, name='account'),
    path('item_details/<int:pk>/', views.details, name='item_details'),
    path('view_account/<int:pk>/', views.view_account, name='view_account'),
    path('item/delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('sold/<int:pk>/', views.sold_item, name='sold_item'),
    path('notsold/<int:pk>/', views.notsold_item, name='notsold_item'),
    path('filter/item/book/', views.filter_book, name='filter_book'),
    path('filter/item/phone/', views.filter_phone, name='filter_phone'),
    path('filter/item/computer/', views.filter_computer, name='filter_computer'),
    path('filter/item/appliances/', views.filter_appliances, name='filter_appliances'),
    path('filter/item/gadget/', views.filter_gadget, name='filter_gadget'),
    path('filter/item/furniture/', views.filter_furniture, name='filter_furniture'),
    path('filter/item/apartment/', views.filter_apartment, name='filter_apartment'),
    path('filter/item/clothing/', views.filter_clothing, name='filter_clothing'),
    path('filter/item/vehicle/', views.filter_vehicle, name='filter_vehicle'),
    path('filter/item/kitchen/', views.filter_kitchen, name='filter_kitchen'),
    path('filter/item/others/', views.filter_others, name='filter_others'),


    path('search/items/', views.search_item, name='search_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
