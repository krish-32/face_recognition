# Generated by Django 5.0.6 on 2024-06-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0027_alter_staff_register_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
