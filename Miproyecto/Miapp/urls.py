
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('material/', views.material, name='material'),
    path('inventory/', views.inventory_view, name='inventory'),
    path('delete/<int:id>/', views.delete_material, name='delete_material'),
    path('material/<int:id>/editar/', views.edit_material, name='edit_material'),  
] 