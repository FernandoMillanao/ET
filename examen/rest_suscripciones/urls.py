from django.urls import path
from rest_suscripciones.views import lista_registro

urlpatterns = [
    path('lista_registro', lista_registro, name="lista_registro"),
]