# Generated by Django 3.1 on 2020-08-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200824_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_alternntive',
            name='PALNAlternative',
            field=models.ManyToManyField(related_name='product_alernative', to='products.Product'),
        ),
    ]
