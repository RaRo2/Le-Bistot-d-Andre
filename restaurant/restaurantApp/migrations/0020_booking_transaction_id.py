# Generated by Django 3.1.7 on 2021-06-23 01:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0019_remove_booking_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='transaction_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
