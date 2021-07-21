from django.shortcuts import render
from .models import Flores, Tierradehojas, maceteros


# Create your views here.
def home(request):
    return render(request, 'core/home.html')



def venta(request):
    return render(request, 'core/venta.html')



def venta(request):
    flores= Flores.objects.all()


    datos= {
        'flores': flores
    }




    return render(request, 'core/venta.html', datos)


def venta1(request):
    return render(request, 'core/venta.html')


def venta1(request):
    macetas= maceteros.objects.all()

    datos1= {
        'macetas': macetas
    }

    return render(request, 'core/venta1.html', datos1)


def venta2(request):
    return render(request, 'core/venta2.html')

def venta2(request):
    tierradehojas= Tierradehojas.objects.all()

    datos2= {
        'tierradehojas' : tierradehojas
    }
    return render(request, 'core/venta2.html', datos2)
