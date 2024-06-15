# Generated by Django 5.0.6 on 2024-05-31 22:21

import django.db.models.deletion
import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0010_alter_staff_data_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hod',
            name='password',
        ),
        migrations.RemoveField(
            model_name='hod',
            name='username',
        ),
        migrations.AlterField(
            model_name='hod',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hod',
            name='photo',
            field=models.ImageField(upload_to=pathlib.PureWindowsPath('C:/Users/srikr/Desktop/face_recognition/static/images')),
        ),
        migrations.AlterField(
            model_name='staff_data',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dean.hod'),
        ),
    ]