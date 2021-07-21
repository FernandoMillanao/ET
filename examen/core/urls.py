from django.conf.urls import url
from django.urls import path
from os import name
from .views import home, venta, venta1, venta2


urlpatterns= [
    path('', home,name="home"),
    path('venta', venta,name="ventas"),
    path('venta1', venta1,name="ventas1")

    

]




