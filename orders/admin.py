from django.contrib import admin
from .models import *

class GoodsInOrderInline(admin.TabularInline):
    model = GoodsInOrder
    extra = 0


class CocktailsInOrderInline(admin.TabularInline):
    model = CocktailsInOrder
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    list_display.remove("comments")
    search_fields = [field.name for field in Order._meta.fields]
    inlines = [GoodsInOrderInline, CocktailsInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class GoodsInOrderAdmin(admin.ModelAdmin):

    class Meta:
        model = GoodsInOrder

admin.site.register(GoodsInOrder, GoodsInOrderAdmin)

class CocktailsInOrderAdmin(admin.ModelAdmin):

    class Meta:
        model = CocktailsInOrder

admin.site.register(CocktailsInOrder, CocktailsInOrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    search_fields = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

