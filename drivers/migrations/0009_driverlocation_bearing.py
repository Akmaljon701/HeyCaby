# Generated by Django 4.2.7 on 2023-11-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0008_remove_driverlocation_bearing'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverlocation',
            name='bearing',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
