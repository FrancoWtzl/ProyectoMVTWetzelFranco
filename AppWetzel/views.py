from django.shortcuts import render
from .models import FliaWetzel
from django.http import HttpResponse
from django.template import Template


# Create your views here.
def wetzel(request):

    familia1= FliaWetzel(nombre= "Santiago", apellido= "Wetzel", edad= 58, año_nacimiento= 1964)
    familia1.save()
        
    familia2= FliaWetzel(nombre= "Laura", apellido= "Lazarte", edad= 53, año_nacimiento= 1969)
    familia2.save()
   
    familia3= FliaWetzel(nombre= "Matias", apellido= "Wetzel", edad= 28, año_nacimiento= 1994)
    familia3.save()

    familia4= FliaWetzel(nombre= "Bruno", apellido= "Wetzel", edad= 26, año_nacimiento= 1997)
    familia4.save()

    familia5= FliaWetzel(nombre= "Naiara", apellido= "Wetzel", edad= 23, año_nacimiento= 1999)
    familia5.save()

    familia6= FliaWetzel(nombre= "Tobias", apellido= "Lazarte", edad= 17, año_nacimiento= 2005)
    familia6.save()

    familia= FliaWetzel.objects.all()

    return render(request, "template.html", {"familia" : familia})
    return HttpResponse()