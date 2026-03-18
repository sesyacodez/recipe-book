from django.contrib import admin
from recipes.models import CuisineType, Category, Ingredient, Recipe, SavedRecipe

admin.site.register(CuisineType)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(SavedRecipe)