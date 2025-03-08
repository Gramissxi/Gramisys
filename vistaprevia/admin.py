# Register your models here.

from django.contrib import admin
from vistaprevia.models import Producto, Categoria, Marca

#me va a decir cuantos prouctos extra voy a poner dentro del panel admin dentro de categoria
class ProductoInline(admin.TabularInline):  # se usa para ordenar la vista de categoria, model= Producto es para agregar el obj producto a la variable model
    model= Producto                                                                                      
    extra=0  #es un atributo de tabulariline para poner cuantos add productos queres ver

class CategoriaAdmin(admin.ModelAdmin):
    inlines= [ProductoInline] #atributo reservado le dice a dj que quiere insertar un formulario de un modelo relacionado 
    #agrega productoInline al admin de categoria

@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    #fieldsets nos va a permitir organizar el panel de admin separa en dos relacion y un sub abajo de datos generales
    fieldsets= [
        ("Relación", {"fields": ["categoria", "marca"]}),
        (
        "Datos generales",
        {
            "fields":[
                'nombre', 'stock', 'tamaños', 'tipo', 'fecha_ingreso', 'precio'
            ]
        }
        )
    ]
#listadisplay-> nos va a servir para ordenar en columnas los datos de arriba
    list_display= ['categoria','marca','nombre', 'Stock','tamaños', 'tipo', 'Precio', 'fecha_ingreso', 'upper_case_name']
   
#cambiar el ordenamiento de la tabla
    ordering= ['-fecha_ingreso'] #porque cambia todos los ordenes
    list_filter= ('nombre', 'fecha_ingreso',) #lista los filtros a la derecha
  
    search_fields=('nombre',) #genera un buscador arriba que solamente va a buscar x nombre,categoria y marca 
    #error cuando usar una foreingKey para buscar. como lo es categoria y marca
    #BUSCAR FORMA DE QUE SE PUEDA BUSCAR TAMBIEN POR BEBIDAS O NO SE VA A PODER? 
    
    list_display_links= ('nombre','Stock')#va a permitir modificar apretando el link 
    #aca tambien modificamos porque ahora la funcion falta_sotck es la que no va a devolver el stock
    #le cambie el nombre porque este nombre el de la funcion Stocke()es el que apareceria en la tabla productos 

    
    @admin.display(description='NOMBRE')
    def upper_case_name(self,obj): #para cada objeto voy a visualizarlo de forma tal de obtener el prodcuto y el precio y transformarlo en mayuscula
        return ("%s %s" % (obj.nombre, obj.categoria)).upper()








#admin.site.register(Categoria)


#SOLO ESTE ME INTERESA MOSTRAR LOS ANTERIORES SON TABLAS 

##admin.site.register(Producto,ProductAdmin)  Esta clase ordena el panel de admid para agregar productos de forma ordenada
#lo pude reemplazar usando un decorador antes de la clase @admin.registr(producto)
admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Marca)

