from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('donewithit/', views.items, name='donewithit'),
    path('sell/item/', views.sell_item, name='sell_item'),
    path('account/', views.account, name='account'),
    path('item_details/<int:pk>/', views.details, name='item_details'),
    path('view_account/<int:pk>/', views.view_account, name='view_account'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('sold/<int:pk>/', views.sold_item, name='sold_item'),
    path('notsold/<int:pk>/', views.notsold_item, name='notsold_item'),
    path('filter/item/<Books>/', views.filter_item, name='filter_book'),
    path('search/items/', views.search_item, name='search_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
