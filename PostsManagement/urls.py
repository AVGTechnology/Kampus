from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static
from PostsManagement.views import NewsFeed

urlpatterns = [

    #path("", views.news_feed, name='index'),
    path('', NewsFeed.as_view(),  name="index"),
    path('post/', views.post, name='post'),
    path('like/', views.like, name='like'),
    path('comment/count/', views.comment_count, name='comment_count'),
    path('video/thumbnail/<int:pk>/', views.thumbnail, name='thumbnail'),
    path('comment_view/<int:pk>/', views.comment_view, name='comment_view'),
    path('preview/<int:pk>/', views.preview, name='preview'),
    path('comment/<int:pk>/', views.comment, name='comment'),
    path('likes/<int:pk>/', views.likes, name='likes'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
