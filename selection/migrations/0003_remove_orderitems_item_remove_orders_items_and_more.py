# Generated by Django 4.1.5 on 2023-01-31 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("selection", "0002_items_orderitems_orders"),
    ]

    operations = [
        migrations.RemoveField(model_name="orderitems", name="item",),
        migrations.RemoveField(model_name="orders", name="items",),
        migrations.RemoveField(model_name="orders", name="user",),
        migrations.DeleteModel(name="Items",),
        migrations.DeleteModel(name="OrderItems",),
        migrations.DeleteModel(name="Orders",),
    ]