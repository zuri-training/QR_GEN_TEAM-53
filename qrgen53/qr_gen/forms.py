from django import forms

from .models import QRcode


class QrcodeCreate(forms.ModelForm):
    class Meta:
        model = QRcode
        fields = {
            'title',
            'base_url',
            'type_qr'
        }
