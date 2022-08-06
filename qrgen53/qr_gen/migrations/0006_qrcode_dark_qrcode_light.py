# Generated by Django 4.0.6 on 2022-08-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0005_alter_qrcode_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='dark',
            field=models.CharField(default='black', max_length=15),
        ),
        migrations.AddField(
            model_name='qrcode',
            name='light',
            field=models.CharField(default='white', max_length=15),
        ),
    ]
