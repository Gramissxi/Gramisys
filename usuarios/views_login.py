from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def pagina_login(request):
    params = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            params['login_exitoso'] = True   #aca es para que se cierra la ventana emergente con el script que este ne l login de usuarios
            return render(request, 'usuarios/login.html', params)
        else:
            params['error'] = "Usuario o contraseña incorrectos"
            return render(request, 'usuarios/login.html', params)
    return render(request, 'usuarios/login.html', params)
