# Generated by Django 3.1.7 on 2021-06-23 01:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0017_auto_20210614_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='special_req',
        ),
        migrations.AlterField(
            model_name='booking',
            name='transaction_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
