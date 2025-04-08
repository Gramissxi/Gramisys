
 
from django.urls import path
from vistaprevia import views #estoy diciendo que desde vista previa importo views que es mi controlador secundario

urlpatterns = [
    #en este path no ponemos nada porque estamos llamando a una funcion en todo caso en la urls.py principal gramiSys aclaramos las dos vista
    path('', views.index, name='index'), #funcion index en views 

    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

]


    #si yo pondria perro aca tedria que tener perro al final de vistapreviaperro quedaria . es como que el nombre 
    #que vaya aca debera ser la continuacion del link
