# Generated by Django 2.0.5 on 2018-05-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_goods_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='sale_price',
            new_name='sale_price_10',
        ),
        migrations.AddField(
            model_name='goods',
            name='sale_price_50',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена продажи (за 50мл)'),
        ),
    ]
