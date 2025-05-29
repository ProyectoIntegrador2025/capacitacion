from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from django.utils.text import slugify

from Categorias.models import Categoria
from Recetas.models import Receta
from Recetas.serializers import RecetaSerializer
from django.core.files.storage import FileSystemStorage
import os
from Seguridad.decorators import logueado

from jose import jwt
from django.conf import settings

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class Clase_Recetas_1 (APIView) :
    
    def get (self, request) :
        data = Receta.objects.order_by('-id').all()
        data_JSON = RecetaSerializer(data, many=True)
        return JsonResponse ({"datos" : data_JSON.data}, status = HTTPStatus.OK)
    
    @logueado()
    def post (self, request) :
        #VALIDACIONES PREVIAS
        if request.data.get("nombre") == None or not request.data.get("nombre") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo nombre es obligatorio y debe ser 'nombre'"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get("tiempo") == None or not request.data.get("tiempo") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo tiempo es obligatorio y debe ser 'tiempo'"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get("descripcion") == None or not request.data.get("descripcion") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo descripcion es obligatorio y debe ser 'descripcion'"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get("categoria_id") == None or not request.data.get("categoria_id") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo categoria_id es obligatorio y debe ser 'categoria_id'"}, status = HTTPStatus.BAD_REQUEST)
        
        if Receta.objects.filter(nombre = request.data['nombre']).exists() : #VALIDO QUE NO EXISTA DATO CON IGUAL NOMBRE POR EJ
            return JsonResponse ({"Estado" : "Error", "Mensaje" : f"Ya existe receta con ese nombre, {request.data['nombre']}"}, status = HTTPStatus.BAD_REQUEST)
        
        try :
            Categoria.objects.filter(pk = request.data['categoria_id']).get() #VALIDA QUE LA CATEGORIA QUE ME INGRESA EL USUARIO SEA CORRECTA Y EXISTA
        except Categoria.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No Existe Categoria Con Ese Id"}, status = HTTPStatus.NOT_FOUND)
        
        #CARGADO DE IMAGEN PARA LA RECETA
        fs = FileSystemStorage()
        try : 
            foto = f"{datetime.timestamp(datetime.now())}{os.path.splitext(str(request.FILES['foto']))[1]}"
            if request.FILES['foto'].content_type == 'image/jpeg' or request.FILES['foto'].content_type == 'image/png' : #VALIDACION DE FORMATO MIMETYPE DEL ARCHIVO QUE SE SUBE
                fs.save(f"recetas/{foto}", request.FILES['foto'])
                fs.url(request.FILES['foto'])
            else :
                return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error de formato de la foto."}, status = HTTPStatus.BAD_REQUEST)
        except Exception as e :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error al subir la foto"}, status = HTTPStatus.BAD_REQUEST)
        
        #CREACION DE LA RECETA Y GUARDADO EN LA BASE
        header = request.headers.get('Authorization').split(" ")
        resuelto = jwt.decode(header[1], settings.SECRET_KEY, algorithms=['HS512'])
        
        try :
            Receta.objects.create(nombre = request.data['nombre'], tiempo = request.data['tiempo'], foto = foto, descripcion = request.data['descripcion'], fechaCreacion = datetime.now(), categoria_id = request.data['categoria_id'], user_id = resuelto["id"])
            return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Receta creada con exito"}, status = HTTPStatus.CREATED)
        except Exception  as e :
            raise Http404


class Clase_Recetas_2 (APIView) :
    
    @logueado()
    def get (self, request, Id) :
        try :
            data = Receta.objects.filter(pk=Id).get()
            data_JSON = RecetaSerializer(data)
            return JsonResponse ({"datos" : data_JSON.data}, status = HTTPStatus.OK)
        except Receta.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No Existe Receta Con Ese Id"}, status = HTTPStatus.NOT_FOUND)
     
    @logueado()    
    def put (self, request, Id) :
        try :
            data = Receta.objects.filter(pk=Id).get()
        except Receta.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No Existe Receta Con Ese Id"}, status = HTTPStatus.NOT_FOUND)
        
        if request.data.get("nombre") == None or not request.data.get("nombre") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo nombre es obligatorio y debe ser 'nombre'"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get("tiempo") == None or not request.data.get("tiempo") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo tiempo es obligatorio y debe ser 'tiempo'"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get("descripcion") == None or not request.data.get("descripcion") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo descripcion es obligatorio y debe ser 'descripcion'"}, status = HTTPStatus.BAD_REQUEST)
        
        if request.data.get("categoria_id") == None or not request.data.get("categoria_id") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo categoria_id es obligatorio y debe ser 'categoria_id'"}, status = HTTPStatus.BAD_REQUEST)
        
        if Receta.objects.filter(nombre = request.data['nombre']).exists() : #VALIDO QUE NO EXISTA DATO CON IGUAL NOMBRE POR EJ
            return JsonResponse ({"Estado" : "Error", "Mensaje" : f"Ya existe receta con ese nombre, {request.data['nombre']}"}, status = HTTPStatus.BAD_REQUEST)
        
        try :
            Categoria.objects.filter(pk = request.data['categoria_id']).get() #VALIDA QUE LA CATEGORIA QUE ME INGRESA EL USUARIO SEA CORRECTA Y EXISTA
        except Categoria.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No Existe Categoria Con Ese Id"}, status = HTTPStatus.NOT_FOUND)
        
        try :
            Receta.objects.filter(pk=Id).update(nombre = request.data['nombre'], slug = slugify(request.data['nombre']), tiempo = request.data['tiempo'], descripcion = request.data['descripcion'], categoria_id = request.data['categoria_id'],)
            return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Receta Editada Con Exito"}, status = HTTPStatus.OK)
        except Receta.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No Se Edito La Receta"}, status = HTTPStatus.BAD_REQUEST)
    
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: 'Receta borrada correctamente',
            401: 'No autorizado',
            404: 'No existe receta con ese ID'
        }
    )
    @logueado()   
    def delete (self, request, Id) :
        try :
            data = Receta.objects.filter(pk=Id).get()
        except Receta.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No Existe Receta Con Ese Id"}, status = HTTPStatus.NOT_FOUND)
        
        #BORRAR LA FOTO
        os.remove(f"./uploads/recetas/{data.foto}")
        
        #BORRAR LA RECETA
        Receta.objects.filter(pk=Id).delete()
        return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Receta borrada correctamente"}, status = HTTPStatus.OK)