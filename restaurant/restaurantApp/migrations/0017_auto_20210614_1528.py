# Generated by Django 3.1.7 on 2021-06-14 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0016_remove_order_menuitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='item',
            new_name='menu_item',
        ),
    ]
