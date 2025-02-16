"""
URL configuration for GramiSys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin lo borro porque no lo necesito
 
from django.urls import path
from vistaprevia import views #estoy diciendo que desde vista previa importo views que es mi controlador secundario

urlpatterns = [
    #en este path no ponemos nada porque estamos llamando a una funcion en todo caso en la urls.py principal gramiSys aclaramos las dos vista
    path('', views.index, name='index'), #funcion index en views 
    #si yo pondria perro aca tedria que tener perro al final de vistapreviaperro quedaria . es como que el nombre 
    #que vaya aca debera ser la continuacion del link
]
