from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .calculos import Consultor

@api_view(['GET'])
def domingos(request, *args, **kwargs):
    print(format)
    if request.method == 'GET':
        # FECHA_INICIO = date(1901,1,1)
        # FECHA_FINAL = date(2000,12,31)
        if request.query_params:
            pass