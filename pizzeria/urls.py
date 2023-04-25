from django.urls import path
from django.contrib import admin
from django import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_ventas', views.lista_ventas, name='lista_ventas'),
    path('agregar_ventas', views.agregar_ventas, name='agregar_ventas'),
    path('actualizar_ventas/<int:idPedido>', views.actualizar_ventas, name='actualizar_ventas'),
    path('eliminar_ventas/<int:idPedido>', views.eliminar_ventas, name='eliminar_ventas'),
    path('lista_inventario', views.lista_inventario, name='lista_inventario'),
    path('agregar_inventario', views.agregar_inventario, name='agregar_inventario'),
    path('actualizar_inventario', views.actualizar_inventario, name='actualizar_inventario'),
    path('eliminar_inventario', views.eliminar_inventario, name='eliminar_inventario'),
]

