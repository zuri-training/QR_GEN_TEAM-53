from turtle import title
from django.db import models

# Create your models here.
class QRcode(models.Model):
    title = models.TextField()
    owner = models.TextField()
    date_created = models.TimeField()
    base_url =  models.TextField()
    type_qr = models.TextField()
    stats = models.IntegerField()

