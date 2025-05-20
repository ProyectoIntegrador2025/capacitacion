from django.urls import path
from . import views
from .views import home_inicio

urlpatterns = [
    path('', home_inicio) #Dejar vacio el path es para una pag de inicio o bienvenida por que es que no pusieron nada en particular.
]
