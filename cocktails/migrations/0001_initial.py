# Generated by Django 2.0.5 on 2018-05-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
                ('alcohol', models.BooleanField(default=True, verbose_name='Алкогольный')),
                ('sale_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Цена продажи')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Описание')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В продаже')),
                ('image', models.ImageField(upload_to='Cocktails_images', verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Позиция создана')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Позиция обновлена')),
            ],
            options={
                'verbose_name': 'Коктейль',
                'verbose_name_plural': 'Коктейли',
            },
        ),
    ]
