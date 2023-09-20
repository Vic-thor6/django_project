from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('calzado/', views.calzado, name='calzado'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('relojes/', views.relojes, name='relojes'),
    path('ropa', views.ropa, name='ropa'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
]
