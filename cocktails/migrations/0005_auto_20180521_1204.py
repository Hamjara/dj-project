# Generated by Django 2.0.5 on 2018-05-21 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0004_goodsincocktail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cocktails',
            old_name='sale_price',
            new_name='total',
        ),
    ]