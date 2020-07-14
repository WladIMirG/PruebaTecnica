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
            FECHA_INICIO = request.query_params['initial_date']
            FECHA_FINAL = request.query_params['final_date']
            DAY = request.query_params['wday']
            cons = Consultor(initial_date=FECHA_INICIO, final_date=FECHA_FINAL, nds=DAY)
        else:
            cons = Consultor()
        msg, inid, find, nday, dayn = cons.domingos()

        return Response({"Mensaje":msg,
                            "initial_date":inid,
                            "final_date":find,
                            "count":nday,
                            "day name":dayn})
