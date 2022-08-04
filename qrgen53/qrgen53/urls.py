"""qrgen53 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import home_view, contact_view, about_view
from accounts.views import register_view, login_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('contact us/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard')
    # path('', include('home.urls')),
    #path('register/', include('django.contrib.auth.urls'))

]

urlpatterns += staticfiles_urlpatterns()
# path('', views.home, name='home')