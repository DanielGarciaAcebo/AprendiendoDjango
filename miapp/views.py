from django.shortcuts import render,HttpResponse

# Create your views here.
# MVC = Model see controller -> Actions (Methods)
# MVT = Model template see -> Actions (Methods)

layout = """
    <h1>Sitio web Django | azul </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/holamundo">Hola mundo</a>
        </li>
        <li>
            <a href="/pagina">pagina</a>
        </li>
    </ul>
"""

def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)} </li>"
        year += 1
    html += "</ul>"

    return HttpResponse(layout + html)


def holamundo(request):
    return HttpResponse(layout + "Hola mundo")

def pagina(request):
    return HttpResponse(layout + "Mi pagina web")

def contacto(request, nombre="", apellidos=""):
    return HttpResponse(layout + f"<h2>Contacto {nombre} {apellidos} </h2>")