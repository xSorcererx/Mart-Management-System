# Generated by Django 4.0.5 on 2022-07-19 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0003_products_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoices',
            name='customer_id',
        ),
    ]
