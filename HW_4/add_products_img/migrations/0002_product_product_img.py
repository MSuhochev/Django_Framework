# Generated by Django 5.0.3 on 2024-03-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("add_products_img", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_img",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
