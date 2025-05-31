from django.shortcuts import render
from django.db.models import Count
from productos.models import Producto, Categoria
from django.views.generic import View
import datetime
from django.shortcuts import redirect

def index(request):
    productos = Producto.objects.all()  
    categorias = Categoria.objects.annotate(total_productos=Count('producto'))  # para contar los productos que hay
    categorias_con_productos = Categoria.objects.prefetch_related('producto_set') #para ver los productos que hay en las categorias del menu de arriba
    params = {
        'nombre_sitio': 'GramiSys',
        'productos': productos,
        'categorias': categorias,
        'categorias_con_productos':categorias_con_productos
        
    }
    return render(request, 'vistaprevia/index.html', params)


def productos_por_categoria(request, categoria_id):
    productos = Producto.objects.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()
    params = {
        'productos': productos,
        'categorias': categorias,
        'categoria_actual': categoria_id,
    }
    return render(request, 'vistaprevia/productos_por_categoria.html', params)

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'vistaprevia/detalle_producto.html', {'producto': producto})

class Templatetags1(View):
    template = "vistaprevia/templatetags1.html"

    def get(self, request):
        params = {}
        params["cross_site_scripting"]= """
            <script> 
            $("*").css({
                "background-color": "yellow",
                "font-weight": "bolder"
            });
            </script>

        """
        

        
        
        productos = Producto.objects.all()  
        params["los_productos"]= productos

        params["fecha_de_hoy"]= datetime.datetime.now()        
        params["mi_lista"]= [1,2,3,4,5]
        params["mi_lista2"]= []
        params["row3"]= "row3"
        return render(request, self.template, params)

    def post(self, request): #para recibir el post con el id y poder crear un carrito
        params= {}
        producto= request.POST.get("producto")
    
        el_pedido= request.session.get("el_pedido")
        if el_pedido:
            cantidad= el_pedido.get(producto)
            if cantidad:
                el_pedido[producto]= cantidad + 1
            else:
                el_pedido[producto]= 1
        else:
            el_pedido= {}
            el_pedido[producto]= 1

        request.session["el_pedido"]= el_pedido

        print(request.session["el_pedido"])
    
        return redirect("templatetags1")


