# Generated by Django 4.0.6 on 2022-08-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0003_alter_qrcode_date_created_alter_qrcode_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='stats',
            field=models.IntegerField(default=0),
        ),
    ]