from django.urls import path
from os import name
from .views import home

urlpatterns= [
    path('', home,name="home"),
    

]

