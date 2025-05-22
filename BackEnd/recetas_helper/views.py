from rest_framework.views import APIView
from django.http.response import JsonResponse
from http import HTTPStatus
from django.http import Http404
from Seguridad.decorators import logueado
from django.contrib.auth.models import User
from Recetas.serializers import *
from Recetas.models import *

from dotenv import load_dotenv
import os
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.

class Clase_Recetas_Helper_1 (APIView) :
    
    def get (self, request) :
        pass


class Clase_Recetas_Helper_2 (APIView) :
    
    def get (self, request, Id) :
        try :
            existe = User.objects.filter(pk = Id).get()
        except User.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El usuario no existe"}, status = HTTPStatus.BAD_REQUEST)
        
        data = Receta.objects.filter(user_id = Id).order_by('-id').all()
        data_json = RecetaSerializer(data, many = True)
        return JsonResponse ({"data" : data_json.data}, status = HTTPStatus.OK)


class Clase_Recetas_Helper_Editar_Foto (APIView) :
    
    @logueado() #CAMBIAR LA FOTO DE UNA RECETA
    def post (self, request) :
        if request.data['id'] == None or not request.data['id'] :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "id incorrecto"}, status = HTTPStatus.BAD_REQUEST)
        
        try :
            existe = Receta.objects.filter(pk = request.data['id']).get()
            anterior = existe.foto
        except Receta.DoesNotExist :
             return JsonResponse ({"Estado" : "Error", "Mensaje" : "No existe tal receta"}, status = HTTPStatus.BAD_REQUEST)
         
        #CARGADO DE IMAGEN PARA LA RECETA
        fs = FileSystemStorage()
        try : 
            foto = f"{datetime.timestamp(datetime.now())}{os.path.splitext(str(request.FILES['foto']))[1]}"
            if request.FILES['foto'].content_type == 'image/jpeg' or request.FILES['foto'].content_type == 'image/png' : #VALIDACION DE FORMATO MIMETYPE DEL ARCHIVO QUE SE SUBE
                fs.save(f"recetas/{foto}", request.FILES['foto'])
                fs.url(request.FILES['foto'])
                Receta.objects.filter(id = request.data['id']).update(foto = foto)
                os.remove(f"./uploads/recetas/{anterior}")
                return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Registro editado correctamente"}, status = HTTPStatus.OK)
            else :
                return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error de formato de la foto."}, status = HTTPStatus.BAD_REQUEST)
        except Exception as e :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Error al subir la foto"}, status = HTTPStatus.BAD_REQUEST)


class Clase_Recetas_Helper_Filtro_Por_Slug_2 (APIView) :
    
    def get (self, request, Slug) :
        try :
            data = Receta.objects.filter(slug = Slug).get()
            data_JSON = RecetaSerializer(data)
            return JsonResponse ({"data" : data_JSON.data}, status = HTTPStatus.OK)
        except Receta.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No existe tal receta"}, status = HTTPStatus.BAD_REQUEST)


class Clase_Recetas_Helper_Listar_Ultimas_3_Recetas (APIView) :
    
    def get (self, request) :
        data = Receta.objects.order_by('-id').all()[:3] #CON EL ORDER BY Y EL ? LO QUE HACE ES QUE ORDENA ALEATORIAMENTE Y SOLO AGARRE LAS ULTIMAS 3 RECETAS ES CON EL [:3]
        data_JSON = RecetaSerializer(data, many = True)
        return JsonResponse ({"data" : data_JSON.data}, status = HTTPStatus.OK)


class Clase_Recetas_Helper_Buscador (APIView) : 
    
    def get (self, request) :
        if request.GET.get('categoria_id') == None or not request.GET.get('categoria_id') :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Debe ingresar categoria"}, status = HTTPStatus.BAD_REQUEST)
        if request.GET.get('search') == None or not request.GET.get('search') :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Debe ingresar search"}, status = HTTPStatus.BAD_REQUEST)
        
        try :
            existe = Categoria.objects.filter(pk = request.GET.get('categoria_id')).get()
        except Categoria.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No existe la categoria"}, status = HTTPStatus.BAD_REQUEST)
        
        try :
            existe = Receta.objects.filter(nombre__icontains = request.GET.get('search')).get()
            data = Receta.objects.filter(categoria_id = request.GET.get('categoria_id')).filter(nombre__icontains = request.GET.get('search')).order_by('-id').all() #BUSCA POR CATEGORIA ID Y POR NOMBRE LIKE...
            data_JSON = RecetaSerializer(data, many = True)
            return JsonResponse ({"data" : data_JSON.data}, status = HTTPStatus.OK)
        except Receta.DoesNotExist :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No existe la receta"}, status = HTTPStatus.BAD_REQUEST)