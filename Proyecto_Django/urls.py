"""
URL configuration for Proyecto_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import bienvenido, bienvenidoRojo
from Proyecto_Django.views import categoriaEdad, obtenerMomentoActual, contenidoHTML, miPrimeraPlantilla, plantillaParametros
from .views import plantillaCargado, plantillaShortcut, plantillaHija1, plantillaHija2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenido),
    path('bienvenida123/', bienvenidoRojo),
    path('categoriaEdad/<int:edad>', categoriaEdad),
    path('momentoActual/', obtenerMomentoActual),
    path('contenido/<nombre>/<int:edad>', contenidoHTML),
    path('plantilla/', miPrimeraPlantilla),
    path('plantillaParametros/', plantillaParametros),
    path('plantillaCargador/', plantillaCargado),
    path('plantillaShort/', plantillaShortcut),
    path('', plantillaHija1),
    path('plantillaHija2/', plantillaHija2),
]
