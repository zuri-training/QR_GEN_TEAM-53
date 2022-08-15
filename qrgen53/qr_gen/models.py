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


class QRcodeWifi(models.Model):
    title = models.CharField(max_length=50, )
    owner = models.CharField(max_length=50, )
    date_created = models.DateField(auto_now=True)
    ssid = models.TextField()
    password = models.TextField()
    security = models.CharField(max_length=6, )
    active = models.BooleanField(default=True)
    light = models.CharField(max_length=15, default='white')
    dark = models.CharField(max_length=15, default='black')
    stats = models.IntegerField(default=0)
    qrcode = models.ImageField(upload_to='media')
    type_qr = models.TextField(default='Wifi')
    tag = models.TextField()


class QRcodeLocation(models.Model):
    title = models.CharField(max_length=50, )
    owner = models.CharField(max_length=50, )
    date_created = models.DateField(auto_now=True)
    long = models.TextField()
    lat = models.TextField()
    active = models.BooleanField(default=True)
    light = models.CharField(max_length=15, default='white')
    dark = models.CharField(max_length=15, default='black')
    stats = models.IntegerField(default=0)
    qrcode = models.ImageField(upload_to='media')
    type_qr = models.TextField(default='Location')
    tag = models.TextField()


class QRcodeEmail(models.Model):
    title = models.CharField(max_length=50, )
    owner = models.CharField(max_length=50, )
    date_created = models.DateField(auto_now=True)
    to = models.TextField()
    subject = models.TextField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    light = models.CharField(max_length=15, default='white')
    dark = models.CharField(max_length=15, default='black')
    stats = models.IntegerField(default=0)
    qrcode = models.ImageField(upload_to='media')
    type_qr = models.TextField(default='Location')
    tag = models.TextField()
