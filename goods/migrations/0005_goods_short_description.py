# Generated by Django 2.0.5 on 2018-05-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20180521_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='short_description',
            field=models.TextField(blank=True, default=None, max_length=70, null=True, verbose_name='Краткое описание'),
        ),
    ]
