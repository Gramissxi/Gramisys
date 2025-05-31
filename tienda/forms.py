from django.forms import ModelForm
from productos.models import Producto

class CargarForm(ModelForm):
    class Meta:
        model= Producto
        fields = ['nombre', 'precio', 'stock', 'categoria','tipo','tamaños','marca','fecha_ingreso', 'imagen']

    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)
        
         