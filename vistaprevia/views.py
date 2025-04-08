from django.shortcuts import render
from django.db.models import Count
from .models import Producto, Categoria

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
