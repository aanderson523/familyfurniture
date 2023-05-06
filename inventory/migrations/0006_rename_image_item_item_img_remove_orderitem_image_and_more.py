# Generated by Django 4.1.5 on 2023-01-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0005_alter_item_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item", old_name="image", new_name="item_img",
        ),
        migrations.RemoveField(model_name="orderitem", name="image",),
        migrations.AddField(
            model_name="orderitem",
            name="images",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="images"
            ),
        ),
    ]
