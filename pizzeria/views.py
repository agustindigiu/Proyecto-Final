from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from .models import Ventas
from .models import Inventario
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
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('correo') and request.POST.get('celular'):
            venta_pedido_old = request.POST.get('pedido')
            venta_old = Ventas()
            venta_old = Ventas.objects.get(pedido = venta_pedido_old)

            vent = Ventas()
            vent.pedido = request.POST.get('pedido')
            vent.nombre = request.POST.get('nombre')
            vent.apellido = request.POST.get('apellido')
            vent.correo = request.POST.get('correo')
            vent.celular = request.POST.get('celular')
            vent.f_registro = venta_old.f_registro
            vent.save()
            return redirect('lista_ventas')
    else:
        sell = Ventas.objects.all()
        datos = { 'ventas' : sell }
    return render(request, 'crud_ventas/actualizar.html', datos)

def eliminar_ventas(request):
    if request.method == 'POST':
        if request.POST.get('pedido'):
            pedido_a_borrar = request.POST.get('pedido')
            tupla = Ventas.objects.get(pedido = pedido_a_borrar)
            tupla.delete()
            return redirect('lista_ventas')
    else:
        sell = Ventas.objects.all()
        datos = { 'ventas' : sell }
        return render(request, 'crud_ventas/eliminar.html', datos)

def lista_inventario(request):
    inv = Inventario.objects.all()
    data = { 'inventario' : inv }
    return render(request, 'crud_inventario/lista.html', data)

def agregar_inventario(request):
    if request.method == 'POST':
        if request.POST.get('codigo') and request.POST.get('producto') and request.POST.get('descripcion') and request.POST.get('unidades'):
            inv = Inventario()
            inv.codigo = request.POST.get('codigo')
            inv.producto = request.POST.get('producto')
            inv.descripcion = request.POST.get('descripcion')
            inv.unidades = request.POST.get('unidades')
            inv.save()
            return redirect('lista_inventario')
    else:
        return render(request, 'crud_inventario/agregar.html')

def actualizar_inventario(request):
    if request.method == 'POST':
        if request.POST.get('producto') and request.POST.get('descripcion') and request.POST.get('unidades'):
            inv_codigo_old = request.POST.get('codigo')
            inv_old = Inventario()
            inv_old = Inventario.objects.get(codigo = inv_codigo_old)

            inv = Inventario()
            inv.codigo = request.POST.get('codigo')
            inv.producto = request.POST.get('producto')
            inv.descripcion = request.POST.get('descripcion')
            inv.unidades = request.POST.get('unidades')
            inv.alta_inventario = inv_old.alta_inventario
            inv.save()
            return redirect('lista_inventario')
    else:
        invent = Inventario.objects.all()
        data = { 'inventario' : invent }
    return render(request, 'crud_inventario/actualizar.html', data)

def eliminar_inventario(request):
    if request.method == 'POST':
        if request.POST.get('codigo'):
            codigo_a_borrar = request.POST.get('codigo')
            tupla = Inventario.objects.get(codigo = codigo_a_borrar)
            tupla.delete()
            return redirect('lista_inventario')
    else:
        invent = Inventario.objects.all()
        data = { 'inventario' : invent }
        return render(request, 'crud_inventario/eliminar.html', data)