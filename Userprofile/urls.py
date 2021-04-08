from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.login, name='login'),
    path('firebase-messaging-sw.js', views.firebase_messaging_sw_js),
    path('fcm/token/', views.update_fcm_token, name='fcm_token'),
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
    path("user_earning/", views.user_earning, name='user_earning'),
    path("edit_profile/", views.edit_profile, name='edit_profile'),
    path("user_profile/<int:pk>", views.view_user_profile, name='view_user_profile'),
    path("create_profile/", views.create_profile, name='create_profile'),
    path("payment/form/", views.paymentform, name='paymentform'),
    path("payment/form/edit/", views.edit_payment, name='edit_payment'),
    path('signup/', views.signup, name='signup'),
    path('discover_account/', views.discover_account, name='discover_account'),
    path('discover_post/', views.discover_post, name='discover_post'),
    path('search/discover/account/', views.search_discover_account, name='search_discover_account'),
    path('search/discover/post/', views.search_discover_post, name='search_discover_post'),
    path("follow/<int:pk>", views.follow, name='follow'),
    path("unfollow/<int:pk>", views.unfollow, name='unfollow'),
    path("follower/<int:pk>", views.followers, name='followers'),
    path("following/<int:pk>", views.followings, name='followings'),
    path("user/edit_username/", views.edit_username, name='edit_username'),
    path("user/edit_image/", views.edit_image, name='edit_image'),
    path("user/edit_profession/", views.edit_profession, name='edit_profession'),
    path("user/edit_phone/", views.edit_phone, name='edit_phone'),
    path("user/edit_name/", views.edit_name, name='edit_name'),
    path("user/edit_dept/", views.edit_dept, name='edit_dept'),
    path("user/edit_school/", views.edit_school, name='edit_school'),

    path("user/username/", views.username, name='username'),
    path("user/name/", views.name, name='name'),
    path("user/profession/", views.profession, name='profession'),
    path("user/phone/", views.phone, name='phone'),
    path("user/image/", views.image, name='image'),
    path("user/dept/", views.dept, name='dept'),
    path("user/school/", views.school, name='school'),
    path("user/requestpay/", views.requestpay, name='requestpay'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
