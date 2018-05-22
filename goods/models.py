from django.db import models


class Goods(models.Model):
    name = models.CharField("Наименование", max_length=256, blank=True, null=True, default=None)
    alcohol = models.BooleanField("Алкоголь", default=True)
    type = models.CharField("Тип", max_length=256, blank=True, null=True, default=None)
    purchase_price = models.DecimalField("Закупочная цена (за 1л)", default=0.00, max_digits=12, decimal_places=2)
    sale_price_10 = models.DecimalField("Цена продажи (за 10мл)", default=0.00, max_digits=12, decimal_places=2)
    sale_price_50 = models.DecimalField("Цена продажи (за 50мл)", default=0.00, max_digits=12, decimal_places=2)
    description = models.TextField("Описание", blank=True, null=True, default=None)
    short_description = models.TextField("Краткое описание", max_length=70, blank=True, null=True, default=None)
    is_active = models.BooleanField("В наличии", default=True)
    image = models.ImageField("Фото", upload_to='Goods_images', blank=True)
    created = models.DateTimeField("Позиция создана", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Позиция обновлена", auto_now_add=False, auto_now=True)

# Create your models here.
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = 'Товары'
