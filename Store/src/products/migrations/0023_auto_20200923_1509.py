# Generated by Django 3.1 on 2020-09-23 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20200905_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PRDBeastsaller',
            new_name='PRDDigital',
        ),
    ]