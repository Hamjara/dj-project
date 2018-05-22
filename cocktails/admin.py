from django.contrib import admin
from .models import *


class GoodsInCocktailInline(admin.TabularInline):
    model = GoodsInCocktail
    extra = 0

class CocktailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cocktails._meta.fields]
    list_display.remove("description")
    list_display.remove("image")
    inlines = [GoodsInCocktailInline]

    search_fields = [field.name for field in Cocktails._meta.fields]

    class Meta:
        model = Cocktails

admin.site.register(Cocktails, CocktailsAdmin)

class GoodsInCocktailAdmin(admin.ModelAdmin):

    class Meta:
        model = GoodsInCocktail

admin.site.register(GoodsInCocktail, GoodsInCocktailAdmin)