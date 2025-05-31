from django.contrib import admin
from .models import Consulta
from .models import Respuesta

class RespuestaInline(admin.TabularInline): #para que es esto
    model = Respuesta
    extra = 0

class ConsultaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display= ['estado_de_respuesta','nombre', 'descripcion', 'mail', 'telefono', 'fecha'] #funcion es estado de respuesta
    list_filter= ['estado_respuesta', 'fecha'] #variuable de la funcion estado de la respuesta
    
admin.site.register(Consulta, ConsultaAdmin)

