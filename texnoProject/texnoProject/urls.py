"""texnoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from texnoApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('features/', views.news_view, name='news_view'),
    path('features/<int:news_id>/', views.news_detail, name='news_detail'),
    path('projects/', views.projects_view, name='projects_view'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('startup/', views.startup_center, name='startup_center'),
    path('startup/<int:startup_id>/', views.startup_detail, name='startup_detail'),
    path('startups/', views.all_startups, name='all_startups'),
    path('contact/', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)