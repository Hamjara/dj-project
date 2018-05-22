# Generated by Django 2.0.5 on 2018-05-21 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180521_1126'),
        ('cocktails', '0003_auto_20180521_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInCocktail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=10, verbose_name='Количество (мл)')),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена за 10мл')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Всего')),
                ('cocktail', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.Cocktails', verbose_name='Коктейль')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='Товар')),
            ],
        ),
    ]
