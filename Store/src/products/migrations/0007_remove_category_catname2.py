# Generated by Django 3.1 on 2020-08-24 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200824_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='CATName2',
        ),
    ]
