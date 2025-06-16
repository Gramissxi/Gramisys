# Register your models here.

from django.contrib import admin
from productos.models import Producto, Categoria, Subcategoria,Marca
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

#me va a decir cuantos prouctos extra voy a poner dentro del panel admin dentro de categoria
class ProductoInline(admin.TabularInline):  # se usa para ordenar la vista de categoria, model= Producto es para agregar el obj producto a la variable model
    model= Producto                                                                                      
    extra=0  #es un atributo de tabulariline para poner cuantos add productos queres ver

class SubcategoriaInline(admin.TabularInline):
    model = Subcategoria
    extra = 0
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [SubcategoriaInline]

class SubcategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]

@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('nombre',)  #excluye el campo nombre del formulario de admin, porque lo vamos a generar automaticamente con el metodo upper_case_name
    #fieldsets nos va a permitir organizar el panel de admin separa en dos relacion y un sub abajo de datos generales
    fieldsets= [
        ("Relación", {"fields": ["subcategoria","marca"]}),
        (
        "Datos generales",
        {
            "fields":[
                'imagen', 'stock', 'tamaños', 'tipo', 'fecha_ingreso', 'precio'
            ]
        }
        )
    ]
#listadisplay-> nos va a servir para ordenar en columnas los datos de arriba

    list_display= ['get_categoria','subcategoria','marca', 'tipo','tamaños', 'stock', 'precio', 'fecha_ingreso', 'upper_case_name']
   

    ordering= ['-fecha_ingreso'] #porque cambia todos los ordenes
    
    
    
    #PROBAR CON NOMBNRE DESP
    search_fields = ('subcategoria__nombre', 'marca__nombre', 'tipo')
    list_filter = ('tipo', 'fecha_ingreso')

    
    
    
    list_display_links= ('upper_case_name','stock')#va a permitir modificar apretando el link 
    actions = ["publicar", "exportar_a_json", "ver_productos"]#el nombre de la accion!!! FUNCION PUBLICAR
    
    def get_categoria(self, obj): #para cada objeto voy a visualizarlo de forma tal de obtener el prodcuto y el precio
        return obj.subcategoria.categoria.nombre  #obj es el objeto que se esta iterando en ese momento, categoria es el campo de la tabla y nombre es el campo de la categoria
    
    get_categoria.short_description = 'Categoria'  #esto es para que se vea el nombre de la columna en el admin
    get_categoria.admin_order_field = 'subcategoria__categoria__nombre'  #esto es para que se pueda ordenar por categoria en el admin




    @admin.display(description='NOMBRE')
    def upper_case_name(self,obj): #para cada objeto voy a visualizarlo de forma tal de obtener el prodcuto y el precio y transformarlo en mayuscula
        tipo = obj.tipo or ''
        return f"{obj.subcategoria} {obj.marca} {tipo}".upper()


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
        productos= Producto.objects.all()  #trae todos los productos de la base de datos
        params["productos"]= productos
        return render(request, "admin/productos/productos.html", params) #aca va a estar la pagina intermedia para ver productos en el admin
                                                                        #lo dejo plasmado pero luego le voy a dar un uso mas funcional
    ver_productos.short_description = "Ver productos"



admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Marca)
admin.site.register(Subcategoria)  # si no se registra no se va a ver en el admin

#def __str__(self):
#    return self.nombre or "Producto sin nombre"
