from django.urls import path
from .views import *

urlpatterns = [
    path('Seguridad/Registro', Clase_Seguridad_Registro_1.as_view()),
    path('Seguridad/Verificacion/<str:token>', Clase_Seguridad_Validacion.as_view()),
    path('Seguridad/LogIn', Clase_Seguridad_LogIn_1.as_view()),
]
