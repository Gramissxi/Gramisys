from django.shortcuts import render
from django.shortcuts import redirect
from productos.models import Producto, Categoria, Marca
from tienda.forms import CargarForm
from django.http import Http404 # para que es?
from django.views.generic import View


def cargar_imagen(request):
    params= {}
    
    
    if request.method== 'POST':
        form= CargarForm(request.POST, request.FILES)
        

        params['form'] = form
        
        if form.is_valid():

            nombre= form.cleaned_data['nombre']
            precio= form.cleaned_data['precio']
            stock= form.cleaned_data['stock']
            categoria= form.cleaned_data['categoria']
            tipo= form.cleaned_data['tipo']
            tamaños= form.cleaned_data['tamaños']
            marca= form.cleaned_data['marca']
            fecha_ingreso= form.cleaned_data['fecha_ingreso']
            imagen= form.cleaned_data['imagen']

            nuevo_producto=Producto(nombre=nombre,precio=precio, stock=stock, categoria=categoria,tipo=tipo,tamaños=tamaños, marca=marca, fecha_ingreso=fecha_ingreso, imagen=imagen)
            nuevo_producto.save()
            return redirect('index')

    else:
        form = CargarForm()
        params['form'] = form 
        params['categorias'] = Categoria.objects.all() #aca agregue esta linea porque tengo tablas de categoria y marca que un encargado de stock se va a encargar
        params['marcas'] = Marca.objects.all() #de cargas desde el panel de admin y la cajera va a directamente cargar un producto segun la categoria y marca que esten ya cargados
        return render(request, 'tienda/formulario.html', params)


class VerImagenes(View):
    template= "tienda/verimagenes.html"

    def get(self, request):
        params={}
        try:
            productos= Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404("No hay productos disponibles") #agregamos mensaje propio para el caso de que no haya productos disponibles  
        params['productos']= productos
        return render(request, self.template, params)
        

def ver_imagen(request, producto_id):
    
    params={}
    try:
        producto= Producto.objects.get(pk= producto_id)
    except Producto.DoesNotExist:
        raise Http404("No hay productos disponibles") #agregamos mensaje propio para el caso de que no haya productos disponibles  

    params['producto']= producto
    return render(request, "tienda/verimagen.html", params)


class EjemploLocalSotage(View):
    template = "tienda/localstorage.html"

    def get(self, request):
        params = {}

        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404("No hay productos disponibles")
        
        params['productos'] = productos
        ###########################
        #PARA INICIALIZAR LA VVARIABLE DE SESSION CARRO
        ##############################################
        try:
            request.session['carro']
        except:
            request.session['carro'] = {}
        
        return render(request, self.template, params)
    