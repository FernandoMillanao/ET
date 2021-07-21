from django.shortcuts import render
from .models import Flores, Tierradehojas, maceteros


# Create your views here.
def home(request):
    return render(request, 'core/home.html')



def venta(request):
    return render(request, 'core/venta.html')



def venta(request):
    flores= Flores.objects.all()
    tierradehojas= Tierradehojas.objects.all()

    datos= {
        'flores': flores
    }







    return render(request, 'core/venta.html', datos)


def venta1(request):
    return render(request, 'core/venta1.html')


def venta1(request):
    macetas= maceteros.objects.all()

    datos= {
        'macetas': macetas
    }

    return render(request, 'core/venta1.html', datos)


