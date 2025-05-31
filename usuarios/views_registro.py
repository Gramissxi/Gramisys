from django.shortcuts import render, redirect
from usuarios.forms import CreateUserForm


def pagina_registro(request):
    params={}
    form= CreateUserForm()
    params['form']= form

    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirigir a la página de inicio después de registrarse
        
    
    
    return render(request, 'usuarios/registro.html', params)
    
