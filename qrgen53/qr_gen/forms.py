from django import forms

from .models import QRcode, Owner, QRcodeWifi, QRcodeLocation, QRcodeEmail


class QrcodeCreate(forms.ModelForm):
    class Meta:
        model = QRcode
        fields = {
            'title',
            'base_url',
            'type_qr',
            'light',
            'dark',
            'tag'
        }


class QrcodeWifiCreate(forms.ModelForm):
    class Meta:
        model = QRcodeWifi
        fields = {
            'title',
            'ssid',
            'password',
            'security',
            'light',
            'dark',
            'tag'
        }


class QrcodeLocationCreate(forms.ModelForm):
    class Meta:
        model = QRcodeLocation
        fields = {
            'title',
            'long',
            'lat',
            'light',
            'dark',
            'tag'
        }


class QrcodeEmailCreate(forms.ModelForm):
    class Meta:
        model = QRcodeEmail
        fields = {
            'title',
            'to',
            'subject',
            'body',
            'light',
            'dark',
            'tag'
        }


class OwnerCreate(forms.ModelForm):
    class Meta:
        model = Owner
        fields = {
            'id',
        }


class AddOwner(forms.ModelForm):
    class Meta:
        model = Owner
        fields = {
            'total_qr',
            'total_active',
        }
