from django.shortcuts import render
from django.shortcuts import redirect
from productos.models import Producto, Subcategoria ,Categoria, Marca
from tienda.forms import CargarForm
from django.http import Http404 # para que es?
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.http import HttpResponse





def cargar_imagen(request):
    params= {}
    
    
    if request.method== 'POST':
        form= CargarForm(request.POST, request.FILES)
        

        params['form'] = form
        
        if form.is_valid():

            subcategoria= form.cleaned_data['subcategoria']
            marca= form.cleaned_data['marca']
            imagen= form.cleaned_data['imagen']
            stock= form.cleaned_data['stock']
            tamaños= form.cleaned_data['tamaños']
            tipo= form.cleaned_data['tipo']
            fecha_ingreso= form.cleaned_data['fecha_ingreso']
            precio= form.cleaned_data['precio']
            

            nuevo_producto=Producto(subcategoria=subcategoria, marca=marca, imagen=imagen, stock=stock, tamaños=tamaños, tipo=tipo, fecha_ingreso=fecha_ingreso, precio=precio)
            nuevo_producto.save()
            return redirect('index')

    else:
        form = CargarForm()
        params['form'] = form 
        params['subcategorias'] = Subcategoria.objects.all() #aca agregue esta linea porque tengo tablas de categoria y marca que un encargado de stock se va a encargar
        params['categorias'] = Categoria.objects.all() #de cargas desde el panel de admin y la cajera va a directamente cargar un producto segun la categoria y marca que esten ya cargados
        params['marcas'] = Marca.objects.all() #de cargas desde el panel de admin y la cajera va a directamente cargar un producto segun la categoria y marca que esten ya cargados
        return render(request, 'tienda/formulario.html', params)

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', producto_id=producto.id)
    else:
        form = CargarForm(instance=producto)

    # Pasás subcategorías y marcas si tu HTML las necesita
    context = {
        'form': form,
        'subcategorias': Subcategoria.objects.all(),
        'marcas': Marca.objects.all(),
        'producto': producto
    }
    return render(request, 'tienda/formulario.html', context)


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
    params['es_staff'] = request.user.is_staff  
    
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



def buscar_productos(request):
    query = request.GET.get('q', '').strip()
    resultados = []

    if len(query) < 2:
        return HttpResponse(status=204) # si apreto me aparece el json vacio asi lo cambie por esto para que no cambie nada si busca vacio

    productos = Producto.objects.filter(nombre__icontains=query)[:5]
    resultados = [
            {
                'nombre': p.nombre,
                'precio': str(p.precio),
                'id': p.id,
                'imagen_url': p.imagen.url if p.imagen else ''
            } for p in productos
        ]

    return JsonResponse(resultados, safe=False)
