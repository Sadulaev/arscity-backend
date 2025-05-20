from django.contrib import admin
from .models import Tile, Laminate, Category, Purpose, Feature

@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'category', 'material', 'room', 'size', 'color', 'surface', 'style', 'country', 'collection', 'is_new', 'is_promo']
    list_filter = ['category', 'material', 'room', 'purpose', 'color', 'surface', 'style', 'features', 'country', 'is_new', 'is_promo']
    search_fields = ['name', 'description']

@admin.register(Laminate)
class LaminateAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'category', 'country', 'grade', 'thickness', 'water_resistant', 'chamfer', 'pattern', 'surface', 'wood_type', 'is_promo']
    list_filter = ['category', 'country', 'grade', 'water_resistant', 'chamfer', 'surface', 'wood_type', 'is_promo']
    search_fields = ['name', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Purpose)
class PurposeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name']
