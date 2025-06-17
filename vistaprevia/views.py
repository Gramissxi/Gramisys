from django.shortcuts import render
from django.db.models import Count
from productos.models import Producto, Categoria
from django.views.generic import View
import datetime
from django.shortcuts import redirect


def index(request):
    productos = Producto.objects.all()  
    categorias = Categoria.objects.annotate(total_productos=Count('subcategorias__productos'))
    categorias = categorias.prefetch_related('subcategorias')
    
    params = {
        'nombre_sitio': 'GramiSys',
        'productos': productos,
        'categorias': categorias,
        'categorias_con_productos': Categoria.objects.prefetch_related('producto_set'),



        'es_staff': request.user.is_staff,  # Verifica si el usuario es staff
    }
    return render(request, 'vistaprevia/index.html', params)


def productos_por_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)  
    productos = Producto.objects.filter(subcategoria__categoria_id=categoria_id)
    categorias = Categoria.objects.all()

    params = {
        'productos': productos,
        'categorias': categorias,
        'categoria': categoria,  
        'es_staff': request.user.is_staff,  # Verifica si el usuario es staff

    }
    return render(request, 'vistaprevia/productos_por_categoria.html', params)

def productos_por_subcategoria(request, subcategoria_id):
    from productos.models import Subcategoria  
    subcategoria = Subcategoria.objects.get(id=subcategoria_id)
    productos = Producto.objects.filter(subcategoria_id=subcategoria_id)
    categorias = Categoria.objects.all()
    return render(request, 'vistaprevia/productos_por_subcategoria.html', {
        'productos': productos,
        'categorias': categorias,
        'subcategoria': subcategoria,
        'es_staff': request.user.is_staff,  # Verifica si el usuario es staff
  
    })

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    categorias = Categoria.objects.all()  
    return render(request, 'vistaprevia/detalle_producto.html', {
        'producto': producto,
        'categorias': categorias })

class Templatetags1(View):
    template = "vistaprevia/templatetags1.html" # la dejo pero no la uso para mi app

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


