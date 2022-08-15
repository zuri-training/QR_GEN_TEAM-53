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

from accounts.views import register_view, login_view, forgot_password_view, new_password_view, recover_password_view, \
    logout_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from home.views import home_view, contact_view, about_view, privacy_policy_view, faq_view, tos_view
from qr_gen.views import qrcode_detail_dy_view, qrcode_create_view, qrcode_delete_view, qrcode_gallery_view, \
    dashboard_view, dashboard_other_view, setting_view, analytics_view, download_file_view, qrcode_wifi_view, \
    qrcode_location_view, qrcode_email_view

# from django_downloadview import ObjectDownloadView


urlpatterns = [
    path('', home_view, name='home'),
    path('contact us/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('privacy-policy/', privacy_policy_view, name='privacy-policy'),
    path('FAQ/', faq_view, name='faq'),
    path('Terms-of-service/', tos_view, name='tos'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('forgot-password/', forgot_password_view, name="forgot-password"),
    path('new-password/', new_password_view, name="new-password"),
    path('recover-password/', recover_password_view, name="recover-password"),

    path('dashboard-main/', dashboard_view, name='dashboard-main'),
    path('dashboard-other/', dashboard_other_view, name='dashboard-other'),
    path('analytics/', analytics_view, name='analytics'),
    path('gallery/', qrcode_gallery_view, name='gallery'),

    path('create/', qrcode_create_view, name='create'),
    path('create-wifi/', qrcode_wifi_view, name='create-wifi'),
    path('create-email/', qrcode_email_view, name='create-email'),
    path('create-location/', qrcode_location_view, name='create-location'),
    path('details/<int:qr_id>/', qrcode_detail_dy_view, name='qr_details'),
    path('details/<int:qr_id>/delete/', qrcode_delete_view, name='qr_delete'),
    path('settings/', setting_view, name='settings'),
    path(r'download/<str:filename>/', download_file_view, name='download'),  # ,include('qrgen.urls')

    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
