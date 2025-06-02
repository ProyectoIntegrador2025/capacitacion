from django.urls import path
from .views import *

urlpatterns = [
    path('Recetas', Clase_Recetas_1.as_view()),
    path('Recetas/<int:Id>', Clase_Recetas_2.as_view())
]
