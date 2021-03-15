from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", views.news_feed, name='index'),
    path('post/', views.post, name='post'),
    path('like/<int:pk>/', views.like, name='like'),
    path('comment_view/<int:pk>/', views.comment_view, name='comment_view'),
    path('comment/<int:pk>/', views.comment, name='comment'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
