from django.urls import path
from .views import *

urlpatterns = [
    path('recetas-panel/Home', Clase_Recetas_Helper_Listar_Ultimas_3_Recetas.as_view()),
    path('recetas-panel', Clase_Recetas_Helper_1.as_view()),
    path('Recetas-Panel/<int:Id>', Clase_Recetas_Helper_2.as_view()),
    path('Recetas-Panel/Recetas-Por-Slug/<str:Slug>', Clase_Recetas_Helper_Filtro_Por_Slug_2.as_view()),
    path('Recetas-Panel/Buscador', Clase_Recetas_Helper_Buscador.as_view()),
    path('Recetas/Editar/Foto', Clase_Recetas_Helper_Editar_Foto.as_view())
]