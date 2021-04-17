"""Kampus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Userprofile.urls")),
    path("", include("PostsManagement.urls")),
    path("", include("Messages.urls")),
    path("", include("StudentGuildian.urls")),
    path("", include("DoneWithIt.urls")),
    path("", include("Management.urls")),
    path('pwa', include('pwa.urls')),
    path("accounts/", include("allauth.urls")),

]


admin.site.site_header = "Kampus Admin"
admin.site.site_title = "Kampus Admin Portal"
admin.site.index_title = "Welcome to Kampus Portal"
