from . import views
from django.urls import path, include
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('message/chat/<int:pk>/', views.chat_page, name='chat_page'),
    path('message/feedback/', views.feedback, name='feedback'),
    path('message/send_chat/<int:pk>/', views.send_chat, name='send_chat'),
    path('message/received_list/', views.received_list, name='received_list'),
    path('message/sent_list/', views.sent_list, name='sent_list'),
    path('message/user_list/', views.message_user_list, name='message_user_list'),
    path('message/search/user_list/', views.search_message_user_list, name='search_message_user_list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
