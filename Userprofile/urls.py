from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.login, name='login'),

    path('accounts/', include('django.contrib.auth.urls')),
    # accounts/ login/ [name='login']
    # accounts/ logout/ [name='logout']
    # accounts/ password_change/ [name='password_change']
    # accounts/ password_change/done/ [name='password_change_done']
    # accounts/ password_reset/ [name='password_reset']
    # accounts/ password_reset/done/ [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/ reset/done/ [name='password_reset_complete']
    path("logout/", views.logout, name='logout'),
    path("user_profile/", views.user_profile, name='user_profile'),
    path("user_profile/<int:pk>", views.view_user_profile, name='view_user_profile'),
    path("create_profile/", views.create_profile, name='create_profile'),
    path('signup/', views.signup, name='signup'),
    path('discover_account/', views.discover_account, name='discover_account'),
    path('discover_post/', views.discover_post, name='discover_post'),
    path('search/discover/account/', views.search_discover_account, name='search_discover_account'),
    path('search/discover/post/', views.search_discover_post, name='search_discover_post'),
    path("follow/<int:pk>", views.follow, name='follow'),
    path("unfollow/<int:pk>", views.unfollow, name='unfollow'),
    path("follower/<int:pk>", views.followers, name='followers'),
    path("following/<int:pk>", views.followings, name='followings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
