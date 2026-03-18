from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
]
