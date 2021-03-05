from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('articles/', views.articles, name='articles'),
    path('like/<int:pk>/', views.like, name='like'),
    path('articles_details/<int:pk>/', views.articles_details, name='articles_details'),
    path('articles_author/<int:pk>/', views.articles_author, name='articles_author'),
    path('create_article', views.create_article, name='create_article'),
    path('add_article', views.add_article, name='add_article'),
    path('search/article/', views.search_article, name='search_article'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
