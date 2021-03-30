from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("management/dashboard/", views.dashboard, name='dashboard'),
    path("management/payment/request/", views.payment_request, name='payment_request'),
    path("management/payment/failed/", views.failed_payment, name='failed_payment'),
    path("management/payment/paid/", views.paid_user, name='paid_user'),
    path("management/kampus/post", views.kampus_post, name='kampus_post'),
    path("management/kampus/users", views.kampus_users, name='kampus_users'),
    path("management/new/users", views.new_user, name='new_user'),
    path("management/user/details/<int:pk>/", views.user_details, name='user_details'),
    path("management/new/post", views.new_post, name='new_post'),
    path("management/donewithit/items", views.donewithit_items, name='donewithit_items'),
    path("management/article/list", views.articles_list, name='articles_list'),
    path("management/new/article", views.new_articles, name='new_articles'),
    path("management/new/items", views.new_items, name='new_items'),
    path("management/item/detail/<int:pk>/", views.item_details, name='items_details'),
    path("management/request/detail/<int:pk>/", views.request_detail, name='request_detail'),
    path("management/request/paid/<int:pk>/", views.paid, name='paid'),
    path("management/request/failed/<int:pk>/", views.failed, name='failed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
