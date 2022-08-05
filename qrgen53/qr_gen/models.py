from turtle import title
from django.db import models


# Create your models here.
class QRcode(models.Model):
    title = models.CharField(max_length=50,)
    owner = models.CharField(max_length=50,)
    date_created = models.DateField(auto_now=True)
    base_url = models.TextField()
    type_qr = models.TextField()
    stats = models.IntegerField(default=0)
