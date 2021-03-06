# Generated by Django 2.0.5 on 2018-05-21 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
        ('orders', '0006_auto_20180518_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='CocktailsInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=1, verbose_name='Количество')),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена за единицу')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Всего')),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cocktails.Cocktails', verbose_name='Товар')),
            ],
        ),
        migrations.AlterField(
            model_name='goodsinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена за 10мл'),
        ),
    ]
