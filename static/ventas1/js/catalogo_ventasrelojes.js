document.addEventListener("DOMContentLoaded", function() {
    const catalogoContainer = document.getElementById("catalogo");

    // los productos
    const productos = [
        { nombre: "Producto 1", precio: 100, imagen: 5},
        { nombre: "Producto 2", precio: 150, imagen: 6},
        { nombre: "Producto 3", precio: 200, imagen: 7},
        { nombre: "Producto 4", precio: 300, imagen: 8},
        { nombre: "Producto 1", precio: 100, imagen: 5},
        { nombre: "Producto 2", precio: 200, imagen: 6},
        { nombre: "Producto 3", precio: 300, imagen: 7},
        { nombre: "Producto 4", precio: 400, imagen: 8},
        { nombre: "Producto 1", precio: 300, imagen: 5},
    ];

    //recorro el array
    productos.forEach(producto => {
        const prod = document.createElement("f");

        prod.innerHTML = `
        
        <div class="col col-custom">
          <img src="${staticBaseUrl}ventas1/img/${producto.imagen}.jpg" class="img-fluid rounded-top" alt="">
          <div class="figure-img">
            <h5>${producto.nombre}</h5>
            <p>$${producto.precio}</p>
            <a name="" id="" class="btn btn-bd-primary" href="#" role="button">Añadir</a>
          </div>
        </div>
        `;

        catalogoContainer.appendChild(prod);
    });
});