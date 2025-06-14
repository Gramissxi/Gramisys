import json
from django.http import HttpResponse
from productos.models import Producto
from django.shortcuts import render
from productos.models import Categoria



def agregar(request, *args, **kwargs):
        if request.method == "GET":
                idproducto = request.GET.get("cada_producto_id")
                valor = request.GET.get("valor")
                carro = request.session.get("carro")
                idproducto_rec = idproducto[:4]
                idproducto_rec = int(idproducto_rec)
                el_prod = Producto.objects.get(id=idproducto_rec)
                print(el_prod.stock)
                print("stock")
                stock_actual= int(el_prod.stock)
                
                if int(valor) >= stock_actual:
                    cantidad = int(valor)
                else:
                    cantidad = int(valor) + 1
 
 # ###########################################
 # ACTUALIZO VARIABLE DE SESSION
 # #################
 
                carro[idproducto] = cantidad
                request.session["carro"]= carro #ACA ESTOY COMUNICANDO DESDE LOCALSTORAGE A MI APP SUPERMARKET
 # ###########################################
 # FIN
 # ###########################################
 
                print(idproducto)
                print(valor)
                print(cantidad)
                print(carro)
                resultados = []
                data = {}
                data["idproducto"] = str(idproducto)
                data["cantidad"] = str(cantidad)
                resultados.append(data)
                data_json = json.dumps(resultados)
                mimetype = "application/json"
                return HttpResponse(data_json, mimetype)
                
def carrito(request):
    carro = request.session.get("carro", {})
    productos = []
    total = 0

    for clave, cantidad in carro.items():
        id_prod = int(''.join(filter(str.isdigit, clave)))
        prod = Producto.objects.get(id=id_prod)
        subtotal = prod.precio * int(cantidad)
        total += subtotal
        productos.append({
            "nombre": prod.nombre,
            "precio": prod.precio,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "imagen": prod.imagen.url if prod.imagen else None
        })

    categorias = Categoria.objects.all()  # <--- agregalo acá

    context = {
        "productos": productos,
        "total": total,
        "categorias": categorias,  # <--- y pasalo al contexto
    }

    return render(request, "tienda/carrito.html", context)
