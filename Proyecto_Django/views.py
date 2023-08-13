from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

#Request: se usa para hacer peticiones
#HttpResponse: Para enviar la respuesta usando el protocolo http.


def bienvenido(request):
    return HttpResponse("Bienvenid@ a este curso de Django")

def bienvenidoRojo(request):
    return HttpResponse("<p style = 'color: red;'>Bienvenid@ a este curso de Django</p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Es una persona de la tercera edad"
        else:
            categoria = "Adultez"

    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolecencia"
    resultado = f"<h1> Categoria de la edad: {categoria}</h1>"
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    #respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    cotenido = f"""
    
    <html>
    <body>
    <p>Nombre: {nombre} / Edad: {edad}</p>    
    </body>
    </html>
    """
    return HttpResponse(cotenido)

def miPrimeraPlantilla(request):
    plantillaExterna = open("C:/Proyecto_Django/Proyecto_Django/plantillas/index.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()

    contexto = Context()
    docuemnto = template.render(contexto)
    return HttpResponse(docuemnto)

def plantillaParametros(request):
    nombre = "Kevin Archila"
    fecha = datetime.datetime.now()
    lenguajes_programacion = ["Python","Ruby","JavaScript","C#","Kotlin"]
    plantillaExterna = open("C:/Proyecto_Django/Proyecto_Django/plantillas/plantillaParametros.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()

    contexto = Context({"Nombre": nombre, "lenguajes": lenguajes_programacion, "fecha": fecha})
    docuemnto = template.render(contexto)
    return HttpResponse(docuemnto)



def plantillaCargado(request):
    nombre = "Kevin Archila"
    fecha = datetime.datetime.now()
    lenguajes_programacion = ["Python","Ruby","JavaScript","C#","Kotlin","PHP"]
    plantillaExterna = loader.get_template('plantillaParametros.html')
    documento = plantillaExterna.render({"Nombre": nombre, "lenguajes": lenguajes_programacion, "fecha": fecha})
    return HttpResponse(documento)



def plantillaShortcut(request):
    nombre = "Kevin Archila"
    fecha = datetime.datetime.now()
    lenguajes_programacion = ["Python","Ruby","JavaScript","C#","Kotlin","PHP","C++"]
    contexto = {"Nombre": nombre, "lenguajes": lenguajes_programacion, "fecha": fecha}
    return render(request, 'plantillaParametros.html', contexto)


def plantillaHija1(request):
    return render(request, "plantillaHija.html")

def plantillaHija2(request):
    return render(request, "plantillaHija2.html")