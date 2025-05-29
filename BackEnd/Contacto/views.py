from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from Contacto.models import Contacto
from http import HTTPStatus
from django.http import Http404
import os

#LLAMAR A UTILIDADES
from Utilidades import Utilidades

#Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class Clase_Contacto_1 (APIView) :
    
    @swagger_auto_schema(
        operation_description='Endopoint para contacto',
        responses={
            200:'Succes',
            400:'Bad request'
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "nombre" : openapi.Schema(type=openapi.TYPE_STRING, description='nombre'),
	            "correo" : openapi.Schema(type=openapi.TYPE_STRING, description='coprreo'),
	            "telefono" : openapi.Schema(type=openapi.TYPE_STRING, description='telefono'),
	            "mensaje" : openapi.Schema(type=openapi.TYPE_STRING, description='mensaje')
            },
            required=['nombre', 'correo', 'telefono', 'mensaje']
        )
    )
    def post (self, request) :
        
        if request.data['nombre'] == '' or not request.data['nombre'] or request.data['nombre'] == None :
            return JsonResponse ({"Estado" : "Error", "mensaje" : "ingrese nombre correctamente"})
        
        if request.data['correo'] == '' or not request.data['correo'] or request.data['correo'] == None :
            return JsonResponse ({"Estado" : "Error", "mensaje" : "ingrese correo correctamente"})
        
        if request.data['telefono'] == '' or not request.data['telefono'] or request.data['telefono'] == None :
            return JsonResponse ({"Estado" : "Error", "mensaje" : "ingrese telefono correctamente"})
        
        if request.data['mensaje'] == '' or not request.data['mensaje'] or request.data['mensaje'] == None :
            return JsonResponse ({"Estado" : "Error", "mensaje" : "ingrese mensaje correctamente"})
        
        try :
            Contacto.objects.create(nombre = request.data['nombre'], correo = request.data['correo'], telefono = request.data['telefono'], mensaje = request.data['mensaje'], fechaMensaje = datetime.now())
            html = f"""
                <h1>Nuevo Mnesaje Registrado</h1>
                <ul>
                    <li>Nombre: {request.data['nombre']}</li>
                    <li>Nombre: {request.data['correo']}</li>
                    <li>Nombre: {request.data['telefono']}</li>
                    <li>Nombre: {request.data['mensaje']}</li>
                </ul>
            """
            Utilidades.SendMail(html, 'Prueba Mail', request.data['correo'])
            return JsonResponse ({"Estado" : "Ok", "mensaje" : "Gracias por su mensaje"}, status = HTTPStatus.CREATED) 
        except Exception as e :
            return JsonResponse ({"Estado" : "Error", "mensaje" : "Error inesperado"}, status = HTTPStatus.BAD_REQUEST) 
        