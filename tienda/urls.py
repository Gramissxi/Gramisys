from django.urls import path
from tienda import views
from tienda.views import VerImagenes
from tienda.views import EjemploLocalSotage
from tienda import views_agregar

urlpatterns = [
    path('cargar/', views.cargar_imagen, name = "cargar"),
    path('<int:producto_id>/ver/', views.ver_imagen, name = "ver"),
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"), # este no lo creo necesario pero lo dejo por si acaso
    path('ejemplo_localstorage/', EjemploLocalSotage.as_view(), name="ejemplo_localstorage"), 
    path('agregar/', views_agregar.agregar, name="agregar"),
    path('carrito/', views_agregar.carrito, name='carrito'),
    path('obtener_desde_localstorage/', views_agregar.productos_desde_localstorage, name='obtener_desde_localstorage'),
    path('producto/<int:producto_id>/editar/', views.editar_producto, name='editar_producto'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),


    
    
    
]

 

