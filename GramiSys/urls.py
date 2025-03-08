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
from django.contrib import admin  #me permite obtener el panel de administración
from django.urls import path, include  # me permite tener links url AGREGO INCLUDE PARA AGREGAR LA OTRA VISTA

urlpatterns = [
    # ACA ESTAN MIS DOS VISTAS porque una es la admin y la otra front con esto decimos que se 
    #incluya vistaprevia sacada desde la urls secundaria vistaprevia.urls 
    
    path ('vistaprevia', include('vistaprevia.urls')), 
    path('accounts/', include('registration.backends.default.urls')), #config para registro de redux 
    path('admin/', admin.site.urls),
]
