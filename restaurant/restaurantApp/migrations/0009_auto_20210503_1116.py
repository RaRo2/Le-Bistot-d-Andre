# Generated by Django 3.1.7 on 2021-05-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0008_auto_20210503_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='status',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('Entree', 'Entree'), ('Salads', 'Salads'), ('Main Course', 'Main Course'), ('Dessert', 'Dessert'), ('Drinks', 'Drinks')], max_length=200, null=True),
        ),
    ]
