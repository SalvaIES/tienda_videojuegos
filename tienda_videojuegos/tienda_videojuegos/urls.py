from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('buscador/', include('buscador.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('carrito/', include('carrito.urls')),
]
