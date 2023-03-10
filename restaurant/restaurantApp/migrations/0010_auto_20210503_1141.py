# Generated by Django 3.1.7 on 2021-05-03 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0009_auto_20210503_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantApp.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantApp.menuitem'),
        ),
    ]
