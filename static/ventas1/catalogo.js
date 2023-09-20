document.addEventListener("DOMContentLoaded", function() {
    const catalogoContainer = document.getElementById("catalogo");

    // Datos de ejemplo (pueden ser cargados desde una API o base de datos)
    const productos = [
        { nombre: "Producto 1", precio: 100 },
        { nombre: "Producto 2", precio: 150 },
        { nombre: "Producto 3", precio: 200 },
        { nombre: "Producto 4", precio: 300 },
        // ... más productos
    ];

    // Generar tarjetas de producto
    productos.forEach(producto => {
        const card = document.createElement("div");
        card.classList.add("col-sd-1", "mb-2");

        card.innerHTML = `
        <div class="row row-cols-lg-4 row-cols-md-2 row-cols-1">
        <div class="col col-custom">
          <img src="img/1.jpg" class="img-fluid rounded-top" alt="">
          <div class="figure-img">
            <h5>${producto.nombre}</h5>
            <p>$${producto.precio}</p>
            <a name="" id="" class="btn btn-bd-primary" href="#" role="button">Añadir</a>
          </div>
        </div>
        `;

        catalogoContainer.appendChild(card);
    });
});






