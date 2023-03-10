# Generated by Django 3.1.7 on 2021-07-03 10:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0024_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_guests',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
