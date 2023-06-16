# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Perro
from django.shortcuts import render
# v1
# def inicio(request):
#     return HttpResponse("Hola soy tu inicio")


# v2
# def inicio(request):
#     archivo = open(r'/Users/carmeniturbe/Desktop/Coding/mi_primer_django/templates/inicio.html','r')
#     template = Template(archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#                 'mensaje':'Este es el mensaje de inicio... ',
#                 'segundos': segundos,
#                 'segundo_par': segundos%2 == 0,
#                 'listado_de_numeros': list(range(25))
#                 }
#     contexto = Context(diccionario)
#     renderizar_template = template.render(contexto)
#     return HttpResponse(renderizar_template)

# v3
# def inicio(request):
#     # archivo = open(r'/Users/carmeniturbe/Desktop/Coding/mi_primer_django/templates/inicio.html','r')
#     # template = Template(archivo.read())
#     template = loader.get_template('inicio.html')
#     # archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#                 'mensaje':'Este es el mensaje de inicio... ',
#                 'segundos': segundos,
#                 'segundo_par': segundos%2 == 0,
#                 'listado_de_numeros': list(range(25))
#                 }
#     # contexto = Context(diccionario)
#     # renderizar_template = template.render(contexto)
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

# v4
def prueba(request):
    # template = loader.get_template('inicio.html')
    segundos = datetime.now().second
    diccionario = {
                'mensaje':'Este es el mensaje de inicio... ',
                'segundos': segundos,
                'segundo_par': segundos%2 == 0,
                'listado_de_numeros': list(range(25))
                }
    # renderizar_template = template.render(diccionario)
    # return HttpResponse(renderizar_template)
    return render(request,'inicio/prueba.html', diccionario)

def inicio(request):
    return render(request, 'inicio/inicio.html')

def segunda_vista(request):
    return HttpResponse("<h1>Soy la segunda vista!</h1>")

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f"<h1>Fecha actual: {fecha}</h1>")

def saludar(request):
    return HttpResponse("Bienvenido/a")

def bienvenida(request, nombre):
    return HttpResponse(f"Bienvenido/a {nombre.title()} ")

# V1
# def crear_perro(request, nombre, edad):
#     template = loader.get_template('crear_perro.html')
#     perro = Perro(nombre=nombre, edad=edad)
#     perro.save()
#     diccionario = {
#         'perro': perro,
#         'edad': edad, 
#     }
#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

# V2
def crear_perro(request, nombre, edad):
    perro = Perro(nombre=nombre, edad=edad)
    perro.save()
    diccionario = {
        'perro': perro,
        'edad': edad, 
    }
    return render(request,'inicio/crear_perro.html', diccionario)