# Generated by Django 5.0.6 on 2024-05-31 18:06

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0002_alter_staff_data_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_data',
            name='photo',
            field=models.ImageField(upload_to=pathlib.PureWindowsPath('C:/Users/srikr/Desktop/face_recognition/static/images')),
        ),
    ]
