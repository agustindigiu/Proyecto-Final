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
        if request.POST.get('pedido') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('celular'):
            vent = Ventas()
            vent.pedido = request.POST.get('pedido')
            vent.nombre = request.POST.get('nombre')
            vent.apellido = request.POST.get('apellido')
            vent.correo = request.POST.get('correo')
            vent.celular = request.POST.get('celular')
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