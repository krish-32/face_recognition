# Generated by Django 5.0.6 on 2024-06-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0011_remove_hod_password_remove_hod_username_alter_hod_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hod',
            name='Degree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hod',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hod',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='hod',
            name='staff_id',
            field=models.BigIntegerField(),
        ),
    ]