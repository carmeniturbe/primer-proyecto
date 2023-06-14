from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context

# def inicio(request):
#     return HttpResponse("Hola soy tu inicio")

def inicio(request):
    archivo = open(r'C:/Users/carmeniturbe/Desktop/Coding/mi_primer_django/templates/inicio.html','r')
    template = Template(archivo.read())
    archivo.close()
    contexto = context()
    renderizar_template = template.render(contexto)
    return HttpResponse(renderizar_template)

def segunda_vista(request):
    return HttpResponse("<h1>Soy la segunda vista!</h1>")

def fecha_actual(request):
    fecha = datetime.now()
    return HttpResponse(f"<h1>Fecha actual: {fecha}</h1>")

def saludar(request):
    return HttpResponse("Bienvenido/a")

def bienvenida(request, nombre):
    return HttpResponse(f"Bienvenido/a {nombre.title()} ")