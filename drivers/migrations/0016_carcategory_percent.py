# Generated by Django 4.2.7 on 2023-12-22 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0015_delete_driverpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='carcategory',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
