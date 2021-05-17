# Generated by Django 3.1.7 on 2021-05-05 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantApp', '0013_auto_20210503_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu_item',
        ),
        migrations.AddField(
            model_name='category',
            name='category_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantApp.menuitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='menuitem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantApp.menuitem'),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantApp.menuitem')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurantApp.order')),
            ],
        ),
    ]