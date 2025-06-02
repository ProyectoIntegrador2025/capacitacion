from django.urls import path
from .views import *

urlpatterns = [
    path('Categorias', Clase_Categoria_1.as_view()),
    path('Categorias/<int:Id>', Clase_Categoria_2.as_view())
]
