from django.conf import settings
from django.contrib import admin  #me permite obtener el panel de administración
from django.urls import path, include  # me permite tener links url AGREGO INCLUDE PARA AGREGAR LA OTRA VISTA
from django.conf.urls.static import static


urlpatterns = [
    # ACA ESTAN MIS DOS VISTAS porque una es la admin y la otra front con esto decimos que se 
    #incluya vistaprevia sacada desde la urls secundaria vistaprevia.urls 
    
    path ('', include('vistaprevia.urls')), 
    path('accounts/', include('registration.backends.default.urls')), #config para registro de redux 
    
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]