# Generated by Django 3.1.7 on 2021-06-14 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0015_order_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menuitem',
        ),
    ]