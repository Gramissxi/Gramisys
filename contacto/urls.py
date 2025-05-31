from django.urls import path
from contacto import views
from contacto.views import Contacto, MensajeEnviado

urlpatterns = [
    path('', Contacto.as_view(), name= "contacto"),
    path('mensaje_enviado', MensajeEnviado.as_view(), name= "mensaje_enviado"),
]
