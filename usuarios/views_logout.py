from django.shortcuts import redirect
from django.contrib.auth import logout

def pagina_logout(request):
    logout(request)  # Cerrar sesión del usuario
    return redirect('index')  # Redirigir a la página principal
