# Generated by Django 5.0.6 on 2024-05-31 17:34

import django.db.models.deletion
import pathlib
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('staff_id', models.BigIntegerField(default=True)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('phone', models.BigIntegerField(default=True)),
                ('department', models.CharField(default=True, max_length=100)),
                ('Degree', models.CharField(default=True, max_length=100)),
                ('photo', models.ImageField(default=True, upload_to=pathlib.PureWindowsPath('C:/Users/srikr/Desktop/face_recognition/static/images'))),
            ],
        ),
        migrations.CreateModel(
            name='staff_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('staff_id', models.BigIntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone', models.BigIntegerField()),
                ('department', models.CharField(max_length=100)),
                ('Degree', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to=pathlib.PureWindowsPath('C:/Users/srikr/Desktop/face_recognition/static/images'))),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('roll_no', models.BigIntegerField(default=True)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('phone', models.BigIntegerField(default=True)),
                ('department', models.CharField(default=True, max_length=100)),
                ('photo', models.ImageField(default=True, upload_to=pathlib.PureWindowsPath('C:/Users/srikr/Desktop/face_recognition/static/images'))),
                ('parent_no', models.BigIntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='staff_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('confirm_pass', models.CharField(blank=True, max_length=100)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Dean.staff_data')),
            ],
        ),
    ]