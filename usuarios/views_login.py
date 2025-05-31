from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def pagina_login(request):
    params={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Aquí puedes agregar la lógica para autenticar al usuario
        # Por ejemplo, usando el modelo User de Django
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('verimagenes')  # Redirigir a la página de inicio después de iniciar sesión
        else:
            return render(request, 'usuarios/login.html',params)
    return render(request, 'usuarios/login.html', params)