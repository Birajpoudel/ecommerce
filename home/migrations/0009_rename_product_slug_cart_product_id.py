# Generated by Django 4.0.2 on 2022-03-10 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product_slug',
            new_name='product_id',
        ),
    ]
