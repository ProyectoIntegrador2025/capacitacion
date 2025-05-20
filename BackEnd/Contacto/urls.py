from django.urls import path
from .views import *

urlpatterns = [
    path('Contacto', Clase_Contacto_1.as_view()),
    #path('Contacto/<int:Id>', Clase_Contacto_2.as_view())
]
