# Generated by Django 4.0.2 on 2022-03-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_category_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default=0, max_length=300, unique=True),
        ),
    ]
