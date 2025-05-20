from django.urls import path
from . import views
from .views import Class_Prueba1, Class_Prueba1_Parametros, Class_Ejemplo_Upload

urlpatterns = [
    path('Prueba1', Class_Prueba1.as_view()),
    path('Prueba1/<int:Id>', Class_Prueba1_Parametros.as_view()), #SI QUERES MAS PARAMETROS ES /<INT:ID>/<STR:NOMBRE>
    path('Upload', Class_Ejemplo_Upload.as_view()),
]
