# Generated by Django 4.1.5 on 2023-01-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0007_rename_images_orderitem_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="item_img",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="files/images"
            ),
        ),
    ]
