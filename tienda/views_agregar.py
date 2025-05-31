import json
from django.http import HttpResponse
from productos.models import Producto

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
                
