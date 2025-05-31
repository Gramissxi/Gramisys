# Register your models here.

from django.contrib import admin
from productos.models import Producto, Categoria, Sub_categoria,Marca
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

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
        ("Relación", {"fields": ["categoria", "subcategoria","marca"]}),
        (
        "Datos generales",
        {
            "fields":[
                'nombre','imagen', 'stock', 'tamaños', 'tipo', 'fecha_ingreso', 'precio'
            ]
        }
        )
    ]
#listadisplay-> nos va a servir para ordenar en columnas los datos de arriba
    list_display= ['categoria','marca','nombre', 'Stock','tamaños', 'tipo', 'Precio', 'fecha_ingreso', 'upper_case_name']
   

    ordering= ['-fecha_ingreso'] #porque cambia todos los ordenes
    list_filter= ('nombre', 'fecha_ingreso',) #lista los filtros a la derecha
  
    search_fields=('nombre',) #genera un buscador arriba que solamente va a buscar x nombre,categoria y marca 
    
    list_display_links= ('nombre','Stock')#va a permitir modificar apretando el link 
    actions = ["publicar", "exportar_a_json", "ver_productos"]#el nombre de la accion!!! FUNCION PUBLICAR
    

    
    @admin.display(description='NOMBRE')
    def upper_case_name(self,obj): #para cada objeto voy a visualizarlo de forma tal de obtener el prodcuto y el precio y transformarlo en mayuscula
        return ("%s %s" % (obj.nombre, obj.categoria)).upper()


    def publicar(self, request, queryset): #cambie en el parametro modeladmin por self porque ahora esta dentro de la clase ProductAdmin
        registro=queryset.update(tipo="Clasica")  #actualiza el campo tipo como podria ser tamaño a clasica
                                         #en este caso a mi no me sirve porque no es funcional para mi app pero lo anoto para que se entienda 
        
        if registro == 1:
            mensaje= "1 registro actualizado"
        else:
            mensaje= "%s registros actualizados" % registro
        
        self.message_user(request, "%s exitosamente" % mensaje)  #es apra que se muestre un mensaje al actualizar el tipo a clasica

    publicar.short_description = "Pasar a clasica"  #descripcion del boton que se va a ver en el admin
    
    def exportar_a_json(self, request, queryset): #sirve para visualizar todos los productos en formato json esto se puede trabajar de muchas formas 
        response = HttpResponse(content_type='application/json') #usamos funciones especificas de httpresponse
        serializers.serialize('json', queryset, stream=response) #serialize es una funcion especifica de json
        return response

    def ver_productos(self, request, queryset): # pagina intermedia para eso creamos carpeta rpoductos 
        params={}
        productos= Producto.objects.all
        params["productos"]= productos
        return render(request, "admin/productos/productos.html", params) #aca va a estar la pagina intermedia para ver productos en el admin
                                                                        #lo dejo plasmado pero luego le voy a dar un uso mas funcional
    ver_productos.short_description = "Ver productos"

admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Marca)
admin.site.register(Sub_categoria)  # si no se registra no se va a ver en el admin

