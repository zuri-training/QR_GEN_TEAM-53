from django.db import models


# Create your models here.
class QRcode(models.Model):
    title = models.CharField(max_length=50, )
    owner = models.CharField(max_length=50, )
    date_created = models.DateField(auto_now=True)
    base_url = models.TextField()
    tag = models.TextField()
    type_qr = models.TextField()
    active = models.BooleanField(default=True)
    light = models.CharField(max_length=15, default='white')
    dark = models.CharField(max_length=15, default='black')
    stats = models.IntegerField(default=0)
    qrcode = models.ImageField(upload_to='media')

    def get_absolute_url(self):
        return f"/details/{self.id}/"


class Owner(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    total_qr = models.IntegerField(default=1)
    total_active = models.IntegerField(default=1)
    total_clicks = models.IntegerField(default=0)
