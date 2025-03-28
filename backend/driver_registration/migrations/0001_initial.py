# Generated by Django 5.1.7 on 2025-03-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=50)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('seats_available', models.PositiveIntegerField()),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(blank=True, max_length=30)),
                ('license_plate', models.CharField(max_length=20)),
                ('seats', models.PositiveIntegerField()),
            ],
        ),
    ]
