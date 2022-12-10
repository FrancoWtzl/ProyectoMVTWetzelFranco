from django.shortcuts import render
from .models import FliaWetzel
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


# Create your views here.
def wetzel(request):

    familia= FliaWetzel(nombre= "Santiago", apellido= "Wetzel", edad= 58)
    familia.save()
    familia_cadena= f"Mi papa se llama {familia.nombre} {familia.apellido}, tiene {familia.edad} años"
    
    familia1= FliaWetzel(nombre= "Laura", apellido= "Lazarte", edad= 53)
    familia1.save()
    familia_cadena1= f"Mi Mama se llama {familia1.nombre} {familia1.apellido}, tiene {familia1.edad} años"

    familia2= FliaWetzel(nombre= "Matias", apellido= "Wetzel", edad= 28)
    familia2.save()
    familia_cadena2= f"Mi hermano se llama {familia2.nombre} {familia2.apellido}, tiene {familia2.edad} años"

    familia3= FliaWetzel(nombre= "Bruno", apellido= "Wetzel", edad= 26)
    familia3.save()
    familia_cadena3= f"Mi hermano se llama {familia3.nombre} {familia3.apellido}, tiene {familia3.edad} años"

    familia4= FliaWetzel(nombre= "Naiara", apellido= "Wetzel", edad= 23)
    familia4.save()
    familia_cadena4= f"Mi hermana se llama {familia4.nombre} {familia4.apellido}, tiene {familia4.edad} años"

    familia5= FliaWetzel(nombre= "Tobias", apellido= "Lazarte", edad= 17)
    familia5.save()
    familia_cadena5= f"Mi hermano se llama {familia5.nombre} {familia5.apellido}, tiene {familia5.edad} años"
    return HttpResponse(familia_cadena, familia_cadena1, familia_cadena2, familia_cadena3, familia_cadena4, familia_cadena5)