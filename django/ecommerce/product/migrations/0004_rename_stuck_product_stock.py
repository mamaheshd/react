# Generated by Django 5.0.1 on 2024-01-16 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stuck',
            new_name='stock',
        ),
    ]