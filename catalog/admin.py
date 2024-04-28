from django.contrib import admin
from catalog.models import Product, Category, Versions


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_per_unit')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Versions)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "version_number",
        "version_name",
        "is_current",
    )
