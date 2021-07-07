from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from HOME.models import Productos, Categorias
from HOME.forms import FormularioNuevoProducto

# Create your views here.
def index(request):
    productos =  Productos.objects.all()
    rproductos = Productos.objects.all().order_by("-id")
    ultimos3 = rproductos[:3]
    ultimos10 = rproductos[:10]
    resto = rproductos[3:10]
    return render(request,"HOME/index.html", {
        "productos": productos,
        "ultimos3":ultimos3,
        "ultimos10":ultimos10,
        "rproductos":rproductos,
        "resto":resto,
        
    })

def acercade(request):
    return render(request, "HOME/acercaDe.html")

def carro(request):
    return render(request, "HOME/carro.html")

def categorias(request):
    return render(request, "HOME/categorias.html", {
        "categorias": Categorias.objects.all()
    })

#def nuevo_producto(request):
 #   return render(request, "HOME/nuevo-producto.html", {
 #       "productos": Productos.objects.all() 
 #   })

def resultados(request):
    return render(request, "HOME/resultados.html",{
        "lista_productos": Productos.objects.all()
    })

def producto(request, producto_id):
    producto=Productos.objects.get(id=producto_id)
    return render(request, "HOME/producto.html", {
        "producto": producto,
    })

def buscar(request):
    if request.GET["producto"]:
        #mensaje="El producto buscado es: %r"  %request.GET["producto"]
            producto=request.GET["producto"]

            if len(producto)>20:
                mensaje="El producto buscado es demasiado largo" 
                return render(request, "HOME/resultados.html", {
                    "mensaje":mensaje})

            else:
                articulos=Productos.objects.filter(titulo__icontains=producto)
                return render(request, "HOME/resultados.html", {
                    "articulos":articulos, 
                    "query":producto })
    else:
        mensaje="No se obtuvieron resultados"
    return HttpResponse(mensaje)

