from django.db import models
from goods.models import Goods
from cocktails.models import Cocktails
from django.db.models.signals import post_save
import decimal
import math


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = 'Статусы заказов'



class Order(models.Model):
    id = models.AutoField("Номер заказа", primary_key=True)
    table_nmb = models.CharField("Номер стола", max_length=64, blank=True, null=True, default=None)
    comments = models.TextField("Комментарий", blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    total = models.DecimalField("Итог", default=0, max_digits=12, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Заказ №{} {}'.format(self.id, self.status.name)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'

class GoodsInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Заказ")
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
        super(GoodsInOrder, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = 'Товары в заказе'



class CocktailsInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Cocktails, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="Товар")
    nmb = models.IntegerField("Количество", default=1)
    price_per_item = models.DecimalField("Цена за единицу", default=0, max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    total_price = models.DecimalField("Всего", default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.product.name)

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.total_price
        self.total_price = self.nmb * self.product.total_price
        super(CocktailsInOrder, self).save(*args, **kwargs)

def goods_in_order_post_save(sender, instance, created, **kwargs):
    all_goods_in_order = GoodsInOrder.objects.filter(order=instance.order, is_active=True)
    all_cocktails_in_order = CocktailsInOrder.objects.filter(order=instance.order, is_active=True)

    order_total_price = 0
    for i in all_cocktails_in_order:
        order_total_price += i.total_price
    for i in all_goods_in_order:
        order_total_price += i.total_price
    print(order_total_price)
    instance.order.total = order_total_price
    instance.order.save(force_update=True)

post_save.connect(goods_in_order_post_save, sender=GoodsInOrder)
post_save.connect(goods_in_order_post_save, sender=CocktailsInOrder)


