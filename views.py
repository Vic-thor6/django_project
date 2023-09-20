from collections import UserDict
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

from ventas1.models import usuario , producto

# Create your views here.
def home(request):
    title = 'PRUEBA_TITULO'
    return render(request,'ventas1/home.html', {
        'mytitle' : title
    })

def iniciarSesion(request):
        if request.method == 'GET':
            return render(request, 'ventas1/content/iniciarSesion.html',{
            'form' : UserCreationForm
        })
        else: 
            if request.method == 'POST':
                print(request.POST)
                user= usuario.objects.get(password = request.POST['clave_usuario'])
    
                login(request,user)
                return render(request,'ventas1/home.html')
    
    
        return render(request,'ventas1/home.html')

def registrar_cliente(request):
    
    if request.method == 'GET':
        return render(request, 'ventas1/content/registrar_cliente.html',{
            'form' : UserCreationForm
        })
    else:
        print('estoy aca', request.POST)
        if request.POST['contrasena'] == request.POST['recontrasena']:            
            user = usuario(
                nombreUsuario=request.POST['nombre'],
                correo=request.POST['correo'],
                password=request.POST['contrasena'],
            )
            user.save()
            return redirect('relojes')
        
    return render(request,'ventas1/content/registrar_cliente.html',{
        'form': UserCreationForm,
        "error": 'Las contraseñas no coinciden'
    })


def catalogo(resquest):
    productos = producto.objects.all()
    return render(resquest,'ventas1/calzado.html',{'productos':productos})

def accesorios(request):
    return render(request,'ventas1/content/accesorios.html')

def calzado(request):
    return render(request,'ventas1/content/calzado.html')

def relojes(request):
    return render(request,'ventas1/content/relojes.html')

def ropa(request):
    return render(request,'ventas1/content/ropa.html')

