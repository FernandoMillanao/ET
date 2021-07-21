from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Registro
from .serializers import RegistroSerializer
@csrf_exempt
@api_view(['GET', 'POST','DELETE'])
def lista_registro(request):
    """"
    Lista de Registros
    """
    if request.method== 'GET':
        registro= Registro.objects.all()
        serializer = RegistroSerializer(registro, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        registro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Create your views here.
