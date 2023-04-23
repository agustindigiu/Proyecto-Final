from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

TEMPLATE_DIR = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, 'index.html')

def lista_ventas(request):
    return render(request, 'crud_ventas/lista.html')

def agregar_ventas(request):
    return render(request, 'crud_ventas/agregar.html')

def actualizar_ventas(request):
    return render(request, 'crud_ventas/actualizar.html')

def eliminar_ventas(request):
    return render(request, 'crud_ventas/eliminar.html')

def lista_inventario(request):
    return render(request, 'crud_inventario/lista.html')

def agregar_inventario(request):
    return render(request, 'crud_inventario/agregar.html')

def actualizar_inventario(request):
    return render(request, 'crud_inventario/actualizar.html')

def eliminar_inventario(request):
    return render(request, 'crud_inventario/eliminar.html')