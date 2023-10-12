# Generated by Django 4.2.6 on 2023-10-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('minimum', models.PositiveIntegerField()),
                ('waiting_cost', models.PositiveIntegerField()),
                ('bonus_percent', models.PositiveIntegerField()),
                ('baggage_cost', models.PositiveIntegerField()),
            ],
        ),
    ]