# Generated by Django 5.0.6 on 2024-06-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_remove_product_category_client_delete_basket_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='responsible_person',
            new_name='responsible_id',
        ),
    ]
