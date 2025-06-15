




function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


// esta funcion es para agregar un producto al localStorage



innerHTML="nuevo texto agregasdo con javascript desde el main.js"

function abrirPopup(url) {
    const w = 600;
    const h = 600;
    const left = (screen.width - w) / 2;
    const top = (screen.height - h) / 2;
    window.open(url, 'popup', `width=${w},height=${h},left=${left},top=${top}`);
}

// Esta función hace la animación con GSAP

function animateCart() {
  const cartCount = document.getElementById('cart-count'); // Asegúrate de que el elemento con id 'cart-count' exista
  gsap.fromTo(cartCount,
    { scale: 1 },
    { scale: 1.5, duration: 0.3, yoyo: true, repeat: 1, ease: "power1.inOut" }
  );
}

function actualizarCarrito() {
  const cartCount = document.getElementById('cart-count');
  if (!cartCount) return;

  let totalProductosDistintos = 0;

  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);

    if (!isNaN(key)) {
      const cantidad = parseInt(localStorage.getItem(key), 10);

      if (!isNaN(cantidad) && cantidad > 0) {
        totalProductosDistintos += 1;  // solo sumo 1 por producto con cantidad > 0
      }
    }
  }

  cartCount.textContent = totalProductosDistintos;

  animateCart();
}

function AgregarI(cada_producto_id, valor) {
    "use strict";
    console.log(cada_producto_id, valor)
    $.ajax({
        beforeSend : function(xhr, settings) { //
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },

        url : "/tienda/agregar/",
        type : "GET",
        data : { cada_producto_id:cada_producto_id, valor:valor},
        success : function(json) {
            console.log(json[0].idproducto.toString());
            console.log(json[0].cantidad.toString());
                    localStorage.setItem(json[0].idproducto.toString(),
json[0].cantidad.toString());
         //location.reload();
        

        let id = json[0].idproducto.toString();
        let cantidad = json[0].cantidad.toString();
        localStorage.setItem(id, cantidad);
        mostrarCantidadesDesdeLocalStorage();
        actualizarCarrito(); // Actualiza y anima el contador

        console.log("ok++++++++++++++++++++++++");
        },
        error : function (xhr, errmsg, err) {
            console.log('Error en carga de respuesta');
        }
        });
}



$('.agregar').click(function (event) { //accedo al objeto del dom agregar/classe en html para manejar el click
 "use strict"; //preguntar para que sirve
    event.preventDefault(); // Evita la prppagacion de eventos no entiendo
    let cada_producto_id = $(this).parent().find('.verid').val(); 
    
    let cantidad_actual = localStorage.getItem(cada_producto_id);
    
    let valor = 1;  // siempre se agrega 1 unidad por clic
    
    if (cantidad_actual !== null) {
        valor = parseInt(cantidad_actual) + 1;
}
    console.log(cada_producto_id);
    console.log(valor);




 //PASO 1: Remuevo todo item que no inicia con utn_
    console.log(JSON.stringify(localStorage)); // verifico que no haya nada en localStorage
    let i;
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        console.log("bbbbbbbb");
        console.log(typeof clave_eliminar); 
        console.log(clave_eliminar);

      //  if(!clave_eliminar.startsWith("utn_")){ //si no empieza con utn_ lo elimino
        //    console.log("retorna NO verdadero !!!!!!!!!!!!!");
            //localStorage.removeItem(clave_eliminar);
          //  console.log("retorna NO verdadero !!!!!!!!!!!!!");
// }
 }
 //PASO 2: Si es la primera vez que se agrega un producto a localStorage, le asigno el valor de 1

 //Si ya existia un valor en la base tomo ese valor en lugar de 1
    if (cantidad_actual !== null) {
    valor = parseInt(cantidad_actual) + 1;
}

AgregarI(cada_producto_id, valor);


}); 

function EliminarUno(cada_producto_id) {
  "use strict";

  let cantidad_actual = localStorage.getItem(cada_producto_id);

  if (cantidad_actual !== null) {
    let nueva_cantidad = parseInt(cantidad_actual) - 1;

    if (nueva_cantidad > 0) {
      localStorage.setItem(cada_producto_id, nueva_cantidad.toString());
    } else {
      localStorage.removeItem(cada_producto_id); // Si llega a 0 o menos, eliminá el producto
    }

    mostrarCantidadesDesdeLocalStorage();
    actualizarCarrito(); // Volvés a actualizar el contador
    console.log("BORRADO desde EliminarUno()");
    console.trace();

  }
}

$('.eliminar').click(function (event) {
  "use strict";
  event.preventDefault();

  let cada_producto_id = $(this).parent().find('.verid').val();
  console.log("Click en botón .eliminar");
  console.trace();

  EliminarUno(cada_producto_id);
});



function mostrarCantidadesDesdeLocalStorage() {
  $('.cantidad-en-carrito').each(function () {
    let id = $(this).data('id').toString();
    let cantidad = localStorage.getItem(id);
    if (cantidad !== null) {
      $(this).text(cantidad);
    } else {
      $(this).text("0");
    }
  });
}


$(document).ready(function () {
  mostrarCantidadesDesdeLocalStorage();
});

//vaciar carrito
$('#vaciar-carrito').click(function () {
    localStorage.clear();
    mostrarCantidadesDesdeLocalStorage();
    actualizarCarrito(); // Actualiza y anima el contador
    alert("Carrito vaciado");
});

















































document.addEventListener('DOMContentLoaded', function() {

    // Función para actualizar el total de la tabla sumando subtotales visibles
    function actualizarTotal() {
        let filas = document.querySelectorAll('tbody tr[data-id]');
        let total = 0;
        filas.forEach(fila => {
            let subtotalTexto = fila.querySelector('td:last-child strong').textContent;
            // Quitar símbolo $ y convertir a número
            let subtotal = parseFloat(subtotalTexto.replace('$', '').replace(',', '.'));
            if (!isNaN(subtotal)) {
                total += subtotal;
            }
        });
        // Actualizar total en el div
        const totalDiv = document.querySelector('.d-flex.justify-content-end.fs-4.fw-bold.mt-3');
        if (totalDiv) {
            totalDiv.textContent = `Total: $${total.toFixed(2)}`;
        }
    }
    
    

    // Al cargar, asegurar que el total está correcto
    actualizarTotal();
    actualizarCarrito();
    


})
