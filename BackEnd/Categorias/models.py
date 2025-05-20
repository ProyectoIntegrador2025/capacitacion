from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Categoria (models.Model) :
    nombre = models.CharField(max_length=20, null=False)
    slug = AutoSlugField(populate_from='nombre')
    
    def __str__(self): #Esto sirve para que cuando llames al modelo sin decirle nada te muestra este campo por defecto!
        return self.nombre
    
    class Meta : #Esta sub clase sirve para generar datos Meta
        db_table = 'Categorias' #Nombre de la tabla
        verbose_name = 'Categoria' #Nombre de los titulos que ve el admin
        verbose_name_plural = 'Categorias' 