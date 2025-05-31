from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuarios.models import Datousuario

@receiver(post_save, sender=User)
def create_datosusuarios(sender, instance, created, **kwargs):
    if created:
        Datousuario.objects.create(usuario=instance)
    else:
        # Para asegurarte de que exista
        Datousuario.objects.get_or_create(usuario=instance) #No estabas creando un nuevo usuario.
                                                            #Django disparó post_save al actualizar User al loguearte, 
                                                            # y tu señal creó un duplicado por error.

@receiver(post_save, sender=User)
def update_datosusuarios(sender, instance, created, **kwargs):
    if created==False:
        instance.datousuario.save()
        print("Se han actualizado los datos del usuario")

#tarea crear una seccion que permita la carga o modificacion de la clase datosusuarios de models en la vista de admin con la html 


#pre_save
#post_save
#@receiver()
