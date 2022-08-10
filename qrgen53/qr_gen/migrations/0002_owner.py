# Generated by Django 4.0.6 on 2022-08-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_gen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('total_qr', models.IntegerField(default=0)),
                ('total_active', models.IntegerField(default=0)),
                ('total_clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
