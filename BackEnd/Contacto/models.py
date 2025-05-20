from django.db import models

# Create your models here.

class Contacto (models.Model) :
    nombre = models.CharField(max_length=25, null=False, blank=False)
    correo = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=9, null=False, blank=False)
    mensaje = models.TextField()
    fechaMensaje = models.DateTimeField()
    #EL BLANK ES PARA Q NO SE PUEDA DEJAR EN BLANCO
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Contacto'
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'