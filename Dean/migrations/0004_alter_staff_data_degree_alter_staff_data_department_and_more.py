# Generated by Django 5.0.6 on 2024-05-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0003_alter_staff_data_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_data',
            name='Degree',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='staff_data',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='staff_data',
            name='phone',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='staff_data',
            name='staff_id',
            field=models.BigIntegerField(blank=True),
        ),
    ]
