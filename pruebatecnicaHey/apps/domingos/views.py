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
        params = request.query_params
        if params.get('initial_date', None) and params.get('final_date', None) :
            FECHA_INICIO = params['initial_date']
            FECHA_FINAL = params['final_date']
            if params.get('wday', None):
                DAY = params['wday']
            else:
                DAY = 'Sunday'
            cons = Consultor(initial_date=FECHA_INICIO, final_date=FECHA_FINAL, nds=DAY)
        else:
            cons = Consultor()
        msg, inid, find, nday, dayn = cons.domingos()

        return Response({"Mensaje":msg,
                            "initial_date":inid,
                            "final_date":find,
                            "count":nday,
                            "day name":dayn})
