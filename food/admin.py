# encoding=UTF-8
from django.contrib import admin
from .models import FoodModel


@admin.register(FoodModel)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'origin_country', 'season',
                    'unit_weight', 'calories', 'protein',
                    'full_fat', 'saturated_fat', 'carbohydrates', 'cellulose')