# Generated by Django 4.1.5 on 2023-01-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_orderitem_image_alter_orderitem_item_delete_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, default="", null=True, upload_to="img"),
        ),
        migrations.AddField(
            model_name="item", name="inventory", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Created"),
                    ("stale", "Stale"),
                    ("paid", "Paid"),
                    ("shipped", "Shipped"),
                    ("instore pickup", "Instore Pickup"),
                    ("refunded", "Refunded"),
                ],
                default="created",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="subtotal",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="order",
            name="tax",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="order",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
