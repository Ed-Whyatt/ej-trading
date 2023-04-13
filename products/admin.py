from django.contrib import admin
from .models import Products, Category


# Exstends admin product views
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'full_name',
        'barcode',
        'price',
        'wholsale_price',
        'sale_price',
    )

    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.
admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
