from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  #activo un protocolo para una vista para eso creo la funcion index


"""
def index(request):
    return HttpResponse("Hola mundo") # esto genera no necesitar un archivo template html es una funcion para uq esimul un xml o html pero no es para una app
    solo es para que devuelva algo y listo  largo no sirve
"""

def index(request):
    params={}
    params['nombre_sitio']= 'GramiSys'
    return render(request,'vistaprevia/index.html', params) #modulo render para que se dirija a encontrar la respues de la 
#request a vista previa cualquier directorio template al archivo index.html y que pase parametros q definan en el dicc
