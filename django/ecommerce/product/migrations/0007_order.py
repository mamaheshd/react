# Generated by Django 4.2.9 on 2024-01-31 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('delivery_status', models.CharField(default='Pending', max_length=255)),
                ('payment_method', models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('Esewa', 'Esewa')], max_length=255)),
                ('payment_status', models.BooleanField(blank=True, default=False, null=True)),
                ('contact_no', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
