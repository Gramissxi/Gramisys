from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField

class ConsultaForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Consulta
        fields = [
            'nombre',
            'descripcion',
            'mail',
            'telefono',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'rows': 3,   # cantidad de filas visibles
                'cols': 40,  # cantidad de columnas visibles (puede omitirse)
                'class': 'form-control',
                'placeholder': 'Escribí una descripción breve...'
            }),
        }
        

    def send_email(self,):
        nombre= self.cleaned_data['nombre']
        descripcion= self.cleaned_data['descripcion']
        mail= self.cleaned_data['mail']
        telefono= self.cleaned_data['telefono']
           
        
        #a partir de aqui logica de envio de mail