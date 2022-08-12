from django import forms

from .models import QRcode, Owner


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
