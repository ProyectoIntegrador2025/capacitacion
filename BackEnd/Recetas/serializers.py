from rest_framework import serializers
from .models import *

class RecetaSerializer (serializers.ModelSerializer) :
    
    categoria = serializers.ReadOnlyField(source='categoria.nombre') #Esto se llama custom data en serializer
    
    fechaCreacion = serializers.DateTimeField(format='%d/%m/%Y') #dia/mes/año
    
    foto = serializers.SerializerMethodField()
    
    user_nombre = serializers.ReadOnlyField(source='user.first_name') #ESTO LO QUE HACE ES QUE USA EL METODO GET DE ABAJO PARA DEVOLVER LA URL DE LA FOTO Y ASI PODER VERLA O USARLA

    
    class Meta :
        model = Receta
        fields = ('id', 'nombre', 'slug', 'tiempo', 'descripcion', 'fechaCreacion', 'categoria_id', 'categoria', 'foto', 'user', 'user_nombre')
    
    def get_foto (self, obj) : #en el obj tenes disponibles todos los campos del modelo
        return f"http://127.0.0.1:8000/uploads/recetas/{obj.foto}"