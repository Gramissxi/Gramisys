from django.db import models
from datetime import datetime
from django.utils.html import format_html

class Consulta(models.Model): 
    
    CONTESTADA= 'Contestada'
    NOCONTESTADA= 'No contestada'
    ENPROCESO= 'En proceso'
    
    ESTADOS = (
        (CONTESTADA, 'Contestada'),
        (NOCONTESTADA, 'No contestada'),
        (ENPROCESO, 'En proceso'),
    )

    nombre= models.CharField(max_length=50, blank=True, null=True)
    descripcion= models.TextField(blank=False, null=False)
    mail= models.EmailField(max_length=50, blank=True, null=True)
    estado_respuesta= models.CharField(max_length=15, blank=True, null=True, choices=ESTADOS, default=NOCONTESTADA)
    telefono=models.CharField(max_length=50, blank=True, null=True)
    fecha=models.DateTimeField(default=datetime.now, blank=True, editable=True)

    def __str__(self,):  #consultar para base
        return self.nombre
    
    def estado_de_respuesta(self, ):
        if self.estado_respuesta== 'Contestada':
            return format_html('<span style= "background-color:#0a0; color:#fff; padding:5px;">{}</span>', self.estado_respuesta,) 

        elif self.estado_respuesta== 'No contestada':
            return format_html('<span style= "background-color:#a00; color:#fff; padding:5px;">{}</span>', self.estado_respuesta,)
       
        elif self.estado_respuesta== 'En proceso':
            return format_html('<span style= "background-color:#F0B203; color:#000; padding:5px;">{}</span>', self.estado_respuesta,)


class Respuesta(models.Model): 
    consulta= models.ForeignKey(Consulta(), on_delete=models.CASCADE, blank=True, null=True) #repasar bases
    respuesta= models.TextField(blank=False, null=False)
    fecha=models.DateTimeField(default=datetime.now, blank=True, editable=True)
  
    def create_mensaje(self,):
        consulta_cambio_estado= Consulta.objects.get(id=self.consulta.id)
        consulta_cambio_estado.estado_respuesta='Contestada'
        consulta_cambio_estado.save()

        #LÓGICA DE ENVIO DE MAIL DE LA RESPUESTA


    def save(self, *args, **kwargs): #args y kwargs
     
        self.create_mensaje() #la funcion va actualizar los datos segun el mensaje de create
        force_update= False
        if self.id:
            force_update=True
        super(Respuesta,self).save(force_update=force_update) 

