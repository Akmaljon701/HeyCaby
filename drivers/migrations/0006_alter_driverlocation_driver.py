# Generated by Django 4.2.7 on 2023-11-13 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0005_alter_driverlocation_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverlocation',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_location', to='drivers.drivers'),
        ),
    ]