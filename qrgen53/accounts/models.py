from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    qr_total: models.PositiveIntegerField(default=0)
    click_total: models.PositiveIntegerField(default=0)
    active_codes: models.PositiveIntegerField(default=0)
