from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    """
    formulario de django para crear un nuevo usuario
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #contra 2 para verificar al registrarse
        