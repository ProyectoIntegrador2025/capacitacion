from datetime import datetime
from rest_framework.views import APIView
#JSON
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.response import Response
#UPLOAD
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.

class Class_Prueba1 (APIView) :
    def get (self, request) :
        #return HttpResponse (f"Metodo GET | Id = {request.GET.get('Id', None)} | slug = {request.GET.get('slug', None)}") #EL REQUEST RECIBE LO QUE VIENE DE LA PETICION HTTP, EL GET LO RECIBE PARA USAR Y CON EL GET() OBTENES EL PARAMETRO POR EL NOMBRE QUE VIENE Y SE LE PUEDE PONER NONE POR SI VIENE VACIO
        #return Response({"Estado" : "Ok", "Mensaje" : f"Metodo GET | Id = {request.GET.get('Id', None)} | slug = {request.GET.get('slug', None)}"}) #DE ESTA FORMA DEVOLVES UN JSON
        return JsonResponse({"Estado" : "Ok", "Mensaje" : f"Metodo GET | Id = {request.GET.get('Id', None)} | slug = {request.GET.get('slug', None)}"}) #ESTA ES LA FORMA DE DEVOLVER JSON QUE RECOMIENDA DJANGO
    
    def post (self, request) :
        if request.data.get('Email') == None or request.data.get('Contraseña') == None :
            raise Http404 #Eso hace que se retorne un error 404
        else:
            return JsonResponse({"Estado" : "Ok", "Mensaje:" : f"Metodo POST | Correo = {request.data.get('Email')} | Contraseña = {request.data.get('Contraseña')}"}, status = 201)

class Class_Prueba1_Parametros (APIView) :
    def get (self, request, Id) : #EL PARAMETRO QUE RECIBE DEBE SER EL MISMO NOMBRE QUE LE PUSISTE EN EL URLS.PY
        return HttpResponse (f"Metodo GET | Parametro = {Id}")
    
    def put (self, request, Id) : #EL PARAMETRO QUE RECIBE DEBE SER EL MISMO NOMBRE QUE LE PUSISTE EN EL URLS.PY
        return HttpResponse (f"Metodo PUT | Parametro = {Id}")
    
    def delete (self, request, Id) : #EL PARAMETRO QUE RECIBE DEBE SER EL MISMO NOMBRE QUE LE PUSISTE EN EL URLS.PY
        return HttpResponse (f"Metodo DELETE | Parametro = {Id}")
    
class Class_Ejemplo_Upload (APIView) :
    def post(self, request) :
        fs = FileSystemStorage()
        fecha = datetime.now()
        foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}" #ESTO LO QUE HACE ES PONERLE UN NOMBRE UNICO A LO QUE SE SUBE POR LA FECHA Y ESTE VALOR ES EL QUE GUARDAS AMS ADELANTE EN LA BD
        fs.save(f"EjemploUpload/{foto}", request.FILES['file'])
        fs.url(request.FILES['file'])
        #CON ESTOS PASOS VOS VAS A PODER ALMACENAR UN ARCHIVO EN EL SERVIDOR!
        return JsonResponse({"Estado" : "Ok", "Mensaje" : "Archivo subido correctamente"})