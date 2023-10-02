from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt




from ventas1.models import Producto,CarritoCompra

# Create your views here.
def home(request):
    title = 'PRUEBA_TITULO'
    return render(request,'ventas1/home.html', {
        'mytitle' : title
    })

def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'ventas1/content/iniciarSesion.html')
    elif request.method == 'POST':
        print(request.POST)
        username = request.POST.get('correo_usuario')
        password = request.POST.get('clave_usuario')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'ventas1/content/iniciarSesion.html', {'error_message': 'Nombre de usuario o contraseña incorrectos.'})
    
    return render(request, 'ventas1/home.html', {'user': request.user})

def cerrarSesion(request):
        logout(request)
        return render(request,'ventas1/home.html')


def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['correo']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        password = request.POST['contrasena']
        email = request.POST['correo']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=nombre ,last_name=apellido)

        login(request, user)

        
        return redirect('ventas1/home.html')

    return render(request, 'ventas1/content/registrar_cliente.html')  

def agregar_al_carrito(request, producto_id):
    # Lógica para agregar un producto al carrito
    # Obtén el producto con el ID proporcionado
    producto = Producto.objects.get(id=producto_id)
    # Añade el producto al carrito del usuario actual
    carrito, creado = CarritoCompra.objects.get_or_create(usuario=request.user)
    carrito.productos.add(producto)
    # Redirige a la página de detalles del producto o al carrito de compra

def ver_carrito(request):
    # Lógica para mostrar el contenido del carrito de compra del usuario actual
    carrito, creado = CarritoCompra.objects.get_or_create(usuario=request.user)
    productos_en_carrito = carrito.productos.all()
    return render(request, 'ventas1/content/carrito.html', {'productos_en_carrito': productos_en_carrito})


def catalogo(resquest):
    productos = Producto.objects.all()
    return render(resquest,'ventas1/calzado.html',{'productos':productos})

def accesorios(request):
    productos = Producto.objects.all()
    return render(request,'ventas1/content/accesorios.html',{'productos':productos})

def calzado(request):
    return render(request,'ventas1/content/calzado.html')

def relojes(request):
    return render(request,'ventas1/content/relojes.html')

def ropa(request):
    productos = Producto.objects.all()
    
    return render(request,'ventas1/content/ropa.html',{'productos':productos})




