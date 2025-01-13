from django.contrib import admin
from .models import DishType, Dish, Chef

admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Chef)
