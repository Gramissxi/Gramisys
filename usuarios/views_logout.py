from django.shortcuts import render
from django.contrib.auth import logout

def pagina_logout(request):
    params={}
    logout(request)  # Cerrar sesión del usuario

    return render(request, 'usuarios/logout.html', params)