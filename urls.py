from django.contrib.auth import views as auth_views
from django.urls import path
from .views import iniciarSesion,crear_usuario,accesorios,calzado,relojes,ropa,home,cerrarSesion,ver_carrito,agregar_al_carrito

urlpatterns = [
    path('', home, name='home'),
    path('accesorios/', accesorios, name='accesorios'),
    path('calzado/', calzado, name='calzado'),
    path('registrar_cliente/', crear_usuario, name='crear_usuario'),
    path('relojes/', relojes, name='relojes'),
    path('ropa', ropa, name='ropa'),
    path('iniciarSesion/', iniciarSesion, name='iniciarSesion'),
    path('logout/', cerrarSesion , name='logout'),
    path('carrito/', ver_carrito , name='carrito'),
]

