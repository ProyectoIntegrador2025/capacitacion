from rest_framework import serializers
from .models import *

class CategoriaSerializer (serializers.ModelSerializer) :
    
    class Meta :
        model = Categoria
        fields = ("id", "nombre", "slug") # podes hacer '__all__' y da todo