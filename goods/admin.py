from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Goods._meta.fields]
    list_display.remove("description")
    list_display.remove("short_description")
    list_display.remove("image")

    search_fields = [field.name for field in Goods._meta.fields]

    class Meta:
        model = Goods

admin.site.register(Goods, GoodsAdmin)
# Register your models here.
