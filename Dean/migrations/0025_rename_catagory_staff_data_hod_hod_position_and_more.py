# Generated by Django 5.0.6 on 2024-06-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0024_alter_hod_photo_alter_staff_data_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_data',
            old_name='catagory',
            new_name='HOD',
        ),
        migrations.AddField(
            model_name='hod',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='staff_data',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
