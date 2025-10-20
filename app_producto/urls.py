# app_producto/urls.py o tu_proyecto/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_productos, name='index'), # Cambiado a index_productos
    # ... otras rutas, también asegúrate de que 'add_producto', 'edit_producto', 'delete_producto' estén correctas
    path('add/', views.add_producto, name='add'),
    path('edit/<int:id>/', views.edit_producto, name='edit'),
    path('delete/<int:id>/', views.delete_producto, name='delete'),
    path('view/<int:id>/', views.view_producto, name='view_producto'),
]