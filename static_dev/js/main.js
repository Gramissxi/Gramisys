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
    
    // Listener para los botones eliminar
    const botonesEliminar = document.querySelectorAll('.eliminar-producto');
    botonesEliminar.forEach(boton => {
        boton.addEventListener('click', function() {
            // Encontrar la fila <tr> padre
            const fila = this.closest('tr[data-id]');
            if (!fila) return;
            

            const idProducto = fila.getAttribute('data-id'); // esto da una string como "2"
            
            localStorage.removeItem(idProducto); // Eliminar del localStorage
            fila.remove();

            // Actualizar total
            actualizarTotal();

            // Opcional: mostrar mensaje si carrito quedó vacío
            const filasRestantes = document.querySelectorAll('tbody tr[data-id]');
            if (filasRestantes.length === 0) {
                const tbody = document.querySelector('tbody');
                tbody.innerHTML = `<tr><td colspan="4" class="text-center">Tu carrito está vacío.</td></tr>`;
                // También puedes ocultar botones o total si quieres
                const totalDiv = document.querySelector('.d-flex.justify-content-end.fs-4.fw-bold.mt-3');
                if (totalDiv) totalDiv.textContent = '';
            }
        });
    });

    // Al cargar, asegurar que el total está correcto
    actualizarTotal();
    actualizarCarrito();
    


})
