# Generated by Django 5.0.6 on 2024-06-01 08:26

import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0018_alter_hod_staff_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(upload_to=pathlib.PureWindowsPath('C:/Users/srikr/Desktop/face_recognition/static/images'))),
            ],
        ),
    ]
