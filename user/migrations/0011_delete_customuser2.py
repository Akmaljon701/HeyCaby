# Generated by Django 4.2.6 on 2023-11-01 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser2',
        ),
    ]