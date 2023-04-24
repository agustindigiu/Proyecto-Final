from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from .models import Ventas
# Create your views here.

TEMPLATE_DIR = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, 'index.html')

def lista_ventas(request):
    sell = Ventas.objects.all()
    datos = { 'ventas' : sell }
    return render(request, 'crud_ventas/lista.html', datos)

def agregar_ventas(request):
    if request.method == 'POST':
        if request.POST.get('Pedidos') and request.POST.get('Nombre') and request.POST.get('Apellido') and request.POST.get('Correo') and request.POST.get('Telefono'):
            vent = Ventas()
            vent.Pedidos = request.POST.get('Pedidos')
            vent.Nombre = request.POST.get('Nombre')
            vent.Apellido = request.POST.get('Apellido')
            vent.Correo = request.POST.get('Correo')
            vent.Telefono = request.POST.get('Telefono')
            vent.save()
            return redirect('lista_ventas')
    else:
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