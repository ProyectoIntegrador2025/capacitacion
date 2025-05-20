from django.shortcuts import render
from datetime import datetime, timedelta
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404, HttpResponseRedirect

from Utilidades import Utilidades as utilidades
#COSAS PARA LOS USUARIOS
from .models import *
from django.contrib.auth.models import User
import uuid
from django.contrib.auth import authenticate
from jose import jwt
from django.conf import settings
import os
import time

# Create your views here.

class Clase_Seguridad_Registro_1 (APIView) :
    
    def post (self, request) :    
        if request.data.get('nombre') == None or not request.data.get('nombre') :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo nombre es obligatorio"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get('correo') == None or not request.data.get('correo') :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo correo es obligatorio"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get('password') == None or not request.data.get('password') :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo password es obligatorio"}, status = HTTPStatus.BAD_REQUEST)
        
        if User.objects.filter(email = request.data['correo']).exists() :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : f"Correo repetido {request.data['correo']}"}, status = HTTPStatus.BAD_REQUEST)
        
        #Creacion Del Token
        token = uuid.uuid4()
        url = f"http://127.0.0.1:8000/API/V1/Seguridad/Verificacion/{token}"
        
        #Registrar al usuario con insert en cascada
        try :
            usuario = User.objects.create_user(username = request.data['nombre'], password = request.data['password'], email = request.data['correo'], is_active = 0) #SOLO PARA CREAR USUARIOS SE USA ESTE METODO
            
            #LOS CAMPOS EN LOS QUE GUARDO LOS DATOS SALEN DE LA BASE DE DATOS y se le puede agregar el first_name y last_name o el is_superuser! Y EL IS_ACTIVE SIRVE PARA QUE EL USUARIO SE CREE SIN PODERSE LOGUEAR A MODO DE QUE TENGA QUE VERIFICARSE
            UsersMetaData.objects.create(token = token, user_id = usuario.id)
            
            #VERIFICACION DE CUENTA VIA CORREO
            html = f"""
                <h3>Verificacion</h3>
                
                hola {request.data['nombre']} , te has registrado correctamente, para poder comenzar a usar tu cuenta haz click en el siguiente enlace: <br/>
                <a href="{url}">Aqui</a>
                <br/>
                o copia y pega la siente url en tu navegador favorito: {url}
            """
            utilidades.SendMail(html, 'Verificacion', request.data['correo'])
            
            return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Registro creado con exito"}, status = HTTPStatus.CREATED)
        except Exception as e :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Ocurrio un error inesperado"}, status = HTTPStatus.BAD_REQUEST)
        

class Clase_Seguridad_Validacion (APIView) :
    
    def get (self, request, token) :
        if token == None or not token :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Recurso No Disponible"}, status = 404)
        
        try :
            data = UsersMetaData.objects.filter(token = token).filter(user__is_active = 0).get() #.filter(user__is_active = 0) accede a la tabla de auth_user de la base y filtra a los que tienen is_active = 0
            
            #LE BORRO EL TOKEN AL USUARIO YA QUE YA SE ACTIVO SU CUENTA
            UsersMetaData.objects.filter(token = token).update(token = "")
            
            #LE MARCO LA CUENTA COMO ACTIVA PARA QUE YA SE PUEDA LOGUEAR
            User.objects.filter(id = data.user_id).update(is_active = 1)
            
            return HttpResponseRedirect("http://127.0.0.1:8000/")
        except UsersMetaData.DoesNotExist :
            raise Http404


class Clase_Seguridad_LogIn_1 (APIView) :
    
    def post (self, request) :
        
        if request.data['correo'] == None or not request.data['correo'] :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error de inicio de sesion"}, status = HTTPStatus.BAD_REQUEST)
            
        if request.data['password'] == None or not request.data['password'] :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error de inicio de sesion"}, status = HTTPStatus.BAD_REQUEST)
           
        #AL TENER UN HASH Y NO LA PASSWORD PRIMERO SE VALIDA EL CORREO Y LUEGO EL PASSWORD 
        try :
            user = User.objects.filter(email = request.data['correo']).get()
        except User.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Credenciales incorrectas"}, status = HTTPStatus.NOT_FOUND)
            
        #VALIDACION DE CONTRASEÑA
        auth = authenticate (request, username = request.data['correo'], password = request.data['password']) #ESTO VALIDA TAMBIEN EL IS_ACTIVE = 1
        
        if auth is not None :
            fecha = datetime.now()
            despues = fecha + timedelta(days=1)
            fechaFinal = int(datetime.timestamp(despues))
            payload = {
                'id' : user.id,
                'ISS' : "http://127.0.0.1:8000",
                'iat' : int(time.time()),
                'ext' : int(fechaFinal)
            }
            try :
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS512')
                return JsonResponse ({"id" : user.id, "nombre" : user.first_name, 'token' : token})
            except Exception as e :
                return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error inesperados"}, status = HTTPStatus.BAD_REQUEST)
        else :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Credenciales incorrectas"}, status = HTTPStatus.NOT_FOUND)
            
        
    
#IMPORTANTE ENTENDER QUE: UserMetadata SON LOS USUARIOS QUE NOSOTROS CREAMOS Y USAMOS EN SI Y user SON LOS USUARIOS QUE SE GUARDAN DE POR SI EN LA BASE,
#SON EL MISMO USUARIO SOLO QUE EN LA BASE SE GUARDAN CON ALGUNA COSITA MAS Y EN EL METADATA LE PONEMOS CON QUE QUEREMOS QUE SE GUARDEN

#IMPORTANTE: EN ESTE LOG IN EL USERNAME TIENE QUE SER EL CORREO, Y NO OTRA COSA, LUEGO SE PEUDE CAMBIAR PERO EN ESTE EJEMPLO QUEDO CON EL USERNAME = CORREO PARA LOGUEARSE

#CONSULTAR POR EL METODO DE LA CONTRASEÑA A GERARDO, SI ESTA BIEN ASI O COMO LO HACEN ELLOS