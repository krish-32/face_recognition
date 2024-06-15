# Generated by Django 5.0.6 on 2024-06-01 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dean', '0014_alter_staff_data_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hod',
            old_name='degree',
            new_name='Degree',
        ),
        migrations.RenameField(
            model_name='staff_data',
            old_name='degree',
            new_name='Degree',
        ),
        migrations.AlterField(
            model_name='hod',
            name='staff_id',
            field=models.BigIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='staff_data',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dean.hod'),
        ),
    ]
