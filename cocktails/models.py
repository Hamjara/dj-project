from django.db import models
from goods.models import Goods
from django.db.models.signals import post_save
import decimal
import math


class Cocktails(models.Model):
    name = models.CharField("Название", max_length=256, default=None, null=True)
    alcohol = models.BooleanField("Алкогольный", default=True)
    total_price = models.DecimalField("Цена продажи", default=0.00, max_digits=12, decimal_places=2)
    description = models.TextField("Описание", blank=True, null=True, default=None)
    in_stock = models.BooleanField("В продаже", default=True, blank=True)
    image = models.ImageField("Фото", upload_to='Cocktails_images', blank=True)
    created = models.DateTimeField("Позиция создана", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Позиция обновлена", auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Коктейль"
        verbose_name_plural = 'Коктейли'
        
        

class GoodsInCocktail(models.Model):
    cocktail = models.ForeignKey(Cocktails, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Коктейль")
    product = models.ForeignKey(Goods, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Товар")
    nmb = models.IntegerField("Количество (мл)", default=10)
    price_per_item = models.DecimalField("Цена за 10мл", default=0, max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    total_price = models.DecimalField("Всего", default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.product.name)

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.sale_price
        self.total_price = decimal.Decimal(math.ceil(self.nmb / 10)) * self.product.sale_price
        super(GoodsInCocktail, self).save(*args, **kwargs)

def goods_in_cocktail_post_save(sender, instance, created, **kwargs):
    all_goods_in_cocktail = GoodsInCocktail.objects.filter(cocktail=instance.cocktail, is_active=True)

    order_total_price = 0
    for i in all_goods_in_cocktail:
        order_total_price += i.total_price

    instance.cocktail.total_price = order_total_price
    instance.cocktail.save(force_update=True)

post_save.connect(goods_in_cocktail_post_save, sender=GoodsInCocktail)
# Create your models here.
