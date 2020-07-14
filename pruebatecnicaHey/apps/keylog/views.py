from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .calculos import KeyLog

@api_view(['GET'])
def keylog(request, *args, **kwargs):
    if request.method == 'GET':
        params = request.query_params
        if params.get('data', None):
            data = params['data']
            data=data.split(',')
            passw = KeyLog(data).passw()
        else:
            passw = KeyLog().passw()
            data = list(KeyLog().data)
        msg = "{0} Es la contraseña mas corta para la los datos suministrados".format(passw)
            
    return Response({"Mensaje":msg,
                    "data":str(data),
                    "password":passw})