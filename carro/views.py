from django.shortcuts import render
from .carro import Carro
from HOME.models import Productos, Categorias
from django.shortcuts import redirect

# Create your views here.
def agregar_producto(request,producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("/carro")

def eliminar_producto(request,producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("/carro")

def restar_producto(request,producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("/carro")

def vaciar_carro(request):
    carro=Carro(request)
    carro.vaciar_carro()
    return redirect("/carro")