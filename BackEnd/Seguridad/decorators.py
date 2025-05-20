from functools import wraps

from django.http import JsonResponse
from http import HTTPStatus
from jose import jwt
from django.conf import settings
from datetime import datetime, timedelta
import time


def logueado () : #ESTO LO QUE VA A HACER ES QUE VA A "PROTEGER" LOS METODOS EN LOS QUE SE USE, VALIDANDO QUE EL USUARIO ESTE LOGUEADO
    def metodo (func) :
        @wraps (func)
        def _decorator (request, *args, **kwargs) :
            
            req = args[0] #ESTO TE TRAE EL REQUEST DEL METODO QUE DECORASTE, OSEA LOS DATOS
            
            if not req.headers.get('Authorization') or req.headers.get('Authorization') == None :
                return JsonResponse ({"Estado" : "Error", "Mensaje" : "Debes iniciar sesion antes de realizar esta accion."}, status = HTTPStatus.UNAUTHORIZED)
            
            header = req.headers.get('Authorization').split(" ")
            
            try :
                PayloadDelToken = jwt.decode(header[1], settings.SECRET_KEY, algorithms=['HS512'])
            except Exception as e :
                return JsonResponse ({"Estado" : "Error", "Mensaje" : "Debes iniciar sesion antes de realizar esta accion."}, status = HTTPStatus.UNAUTHORIZED)
            
            if int(PayloadDelToken["ext"] > int(time.time())) :
                return func(request, *args, **kwargs)
            else :
                return JsonResponse ({"Estado" : "Error", "Mensaje" : "Debes iniciar sesion antes de realizar esta accion."}, status = HTTPStatus.UNAUTHORIZED) 
        return _decorator
    return metodo


#EL METODO SE USA ASI @ Logueado() arriba del def NombreDelMetodo