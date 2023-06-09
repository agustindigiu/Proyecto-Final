from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from .models import Ventas
from .models import Inventario
from django.db.models import Q
# Create your views here.

TEMPLATE_DIR = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
    return render(request, 'index.html')

def lista_ventas(request):
    if request.method == 'POST':
        palabra = request.POST.get('keywords')
        lista = Ventas.objects.all()
        if palabra is not None:
            resultado_busqueda = lista.filter(
                Q(pedido__icontains=palabra) |
                Q(nombre__icontains=palabra) |
                Q(apellido__icontains=palabra) |
                Q(correo__icontains=palabra) |
                Q(celular__icontains=palabra)
            )
            datos = { 'ventas' : resultado_busqueda }
            return render(request, 'crud_ventas/lista.html', datos)
        else:
            datos = { 'ventas' : lista }
            return render(request, 'crud_ventas/lista.html', datos)
    else:
        sell = Ventas.objects.order_by('pedido')[:10]
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

def actualizar_ventas(request, idPedido):
    try:
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
            v = Ventas.objects.get(pedido=idPedido)
            datos = { 'ventas' : sell, 'venta' : v }
            return render(request, 'crud_ventas/actualizar.html', datos)
    except Ventas.DoesNotExist:
        sell = Ventas.objects.all()
        v = None
        datos = { 'ventas' : sell, 'venta' : v }
        return render(request, 'crud_ventas/actualizar.html', datos)


def eliminar_ventas(request, idPedido):
    try:
        if request.method == 'POST':
            if request.POST.get('pedido'):
                pedido_a_borrar = request.POST.get('pedido')
                tupla = Ventas.objects.get(pedido = pedido_a_borrar)
                tupla.delete()
                return redirect('lista_ventas')
        else:
            sell = Ventas.objects.all()
            v = Ventas.objects.get(pedido = idPedido)
            datos = { 'ventas' : sell, 'venta': v }
            return render(request, 'crud_ventas/eliminar.html', datos)
    except Ventas.DoesNotExist:
        sell = Ventas.objects.all()
        v = None
        datos = { 'ventas' : sell, 'venta': v }
        return render(request, 'crud_ventas/eliminar.html', datos)        

def lista_inventario(request):
    if request.method == 'POST':
        word = request.POST.get('keyword')
        list = Inventario.objects.all()
        if word is not None:
            resultado_busqueda = list.filter(
                Q(codigo__icontains=word) |
                Q(producto__icontains=word) |
                Q(descripcion__icontains=word) |
                Q(unidades__icontains=word)
            )
            data = { 'inventario' : resultado_busqueda }
            return render(request, 'crud_inventario/lista.html', data)
        else:
            data = { 'inventario' : list}
            return render(request, 'crud_inventario/lista.html', data)
    else:    
        inv = Inventario.objects.order_by('codigo')[:10]
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

def actualizar_inventario(request, idCodigo):
    try:
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
            prod = Inventario.objects.get(codigo=idCodigo)
            data = { 'inventario' : invent, 'producto' : prod }
            return render(request, 'crud_inventario/actualizar.html', data)
    except Inventario.DoesNotExist:
            invent = Inventario.objects.all()
            prod = None
            data = { 'inventario' : invent, 'producto' : prod }
            return render(request, 'crud_inventario/actualizar.html', data)

def eliminar_inventario(request, idCodigo):
    try:
        if request.method == 'POST':
            if request.POST.get('codigo'):
                codigo_a_borrar = request.POST.get('codigo')
                tupla = Inventario.objects.get(codigo = codigo_a_borrar)
                tupla.delete()
                return redirect('lista_inventario')
        else:
            invent = Inventario.objects.all()
            prod = Inventario.objects.get(codigo=idCodigo)
            data = { 'inventario' : invent, 'producto' : prod }
            return render(request, 'crud_inventario/eliminar.html', data)
    except Inventario.DoesNotExist:
        invent = Inventario.objects.all()
        prod = None
        data = { 'inventario' : invent, 'producto' : prod }
        return render(request, 'crud_inventario/eliminar.html', data)