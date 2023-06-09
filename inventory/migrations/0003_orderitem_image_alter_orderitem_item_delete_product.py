# Generated by Django 4.1.5 on 2023-01-29 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="image",
            field=models.ImageField(blank=True, default="", null=True, upload_to="img"),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="inventory.item",
            ),
        ),
        migrations.DeleteModel(name="Product",),
    ]
