from django.http import Http404
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response

from Recetas.models import Receta
from .models import Categoria
from .serializers import CategoriaSerializer
from http import HTTPStatus
from django.utils.text import slugify

# Create your views here.

class Clase_Categoria_1 (APIView) :
    
    def get (self, request) :
        #SELECT * FROM CATEGORIAS ORDER BY ID DESC
        datos = Categoria.objects.order_by('-id').all()
        datos_Json = CategoriaSerializer(datos, many=True) #EL MANY=TRUE VA SOLO SI QUERES TRAER MUCHOS DATOS
        #return Response (datos_Json.data)
        return JsonResponse ({"datos" : datos_Json.data}, status = HTTPStatus.OK)
    
    def post (self, request) :
        if request.data.get("nombre") == None or not request.data.get("nombre") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo nombre es obligatorio y debe ser 'nombre'"}, status = HTTPStatus.BAD_REQUEST)
        try :
            Categoria.objects.create(nombre = request.data.get("nombre"))
            return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Registro creado exitosamente"}, status = HTTPStatus.CREATED)
        except Exception as e :
            raise Http404
    

class Clase_Categoria_2 (APIView) :
    
    def get (self, request, Id) :
        try :
            #SELECT * FROM CATEGORIAS WHERE ID = 4
            data = Categoria.objects.filter(pk=Id).get() #SOLO EN CASO DE LA ID PODES PONER PK QUE ES LA PRIMARY KEY, DESPUES ES CON EL NOMBRE
            data_Json = CategoriaSerializer(data, many=False)
            return JsonResponse ({"data" : data_Json.data}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist :
            raise Http404
    
    def put (self, request, Id) :
        if request.data.get("nombre") == None or not request.data.get("nombre") :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "El campo nombre es obligatorio y debe ser 'nombre'"}, status = HTTPStatus.BAD_REQUEST)
        try :
            data = Categoria.objects.filter(pk = Id).get()
            Categoria.objects.filter(pk = Id).update(nombre = request.data.get("nombre"), slug = slugify(request.data.get("nombre")))
            return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Updateado correctamente"}, status = HTTPStatus.OK)
        except Categoria.DoesNotExist :
            raise Http404
    
    def delete (self, request, Id) :
        if Id == None :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "Debe brindar un Id"}, status = HTTPStatus.BAD_REQUEST)
        #SE DEBERIA VALIDAR QUE NO HAYA COSAS ASOCIADAS A LA CATEGORIA A ELIMINAR, PERO ESO SE VE MAS ADELANTE
        try :
            data = Categoria.objects.filter(pk = Id).get()
        except Categoria.DoesNotExist :
            raise Http404

        if Receta.objects.filter(categoria_id = Id).exists() :
            return JsonResponse ({"Estado" : "Error", "Mensaje" : "No se pudo eliminar la categoria por que tiene recetas asignadas"}, status = HTTPStatus.BAD_REQUEST)
        
        Categoria.objects.filter(pk = Id).delete()
        return JsonResponse ({"Estado" : "Ok", "Mensaje" : "Eliminado correctamente"}, status = HTTPStatus.OK)