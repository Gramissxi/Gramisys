from django.forms import ModelForm
from productos.models import Producto

class CargarForm(ModelForm):
    class Meta:
        model= Producto
        fields = ['subcategoria', 'marca', 'imagen', 'stock', 'tamaños', 'tipo', 'fecha_ingreso', 'precio']

        def __init__(self, *args, **kwargs):
            self.fields['tipo'].required = False #para que no me obligue a cargar un tipo

            super(CargarForm, self).__init__(*args, **kwargs)
        
         