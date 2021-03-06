# Generated by Django 3.1 on 2020-08-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRDName', models.CharField(max_length=40, verbose_name='Nmae')),
                ('BRBDesc', models.TextField(verbose_name='Brand  Description')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VARName', models.CharField(max_length=40, verbose_name='Nmae')),
                ('VARDesc', models.TextField(verbose_name='Variant  Description')),
            ],
            options={
                'verbose_name': 'Variant',
                'verbose_name_plural': 'VariantS',
            },
        ),
    ]
