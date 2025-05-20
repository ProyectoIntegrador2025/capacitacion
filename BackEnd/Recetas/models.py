from django.db import models
from Categorias.models import Categoria
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.

class Receta (models.Model) :
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING) #ESE DEFAULT 1 HACE QUE LOS CAMPOS QUE YA ESTABAN CREADOS y los que se creen despues SE CREEN CON EL ID 1 OSEA EL ID DEL SUPERADMIN
    nombre = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='nombre', max_length=100)
    tiempo = models.IntegerField()
    foto = models.CharField(max_length=100, null=False) #ESTO ES POR QUE SOLO QUEREMOS GUARDAR EL NOMBRE DE LA FOTO Y NO EL ARCHIVO EN SI POR QUE PESARIA MUCHO
    descripcion = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now=True) #CONFIGURA LA FECHA AUTOMATICAMENTE CON DATETIME
    
    
    def __str__(self):
        return self.nombre
    
    class Meta :
        db_table = 'Recetas'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        
        
        
#TODOS LOS TIPOS DE MODEL. PARA LAS CLAVES FORANEAS SON: (COMPORTAMIENTOS AL HACER DELETE)
#model.DO_NOTHING no hace nada la app, delega en la base de datos
#models.CASCADE	También se eliminan los productos relacionados.
#models.PROTECT	No permite eliminar la categoría si hay productos que la usan.
#models.RESTRICT	Similar a PROTECT, pero más controlado (disponible desde Django 3.1).
#models.SET_NULL	La categoría de los productos se pone en NULL. Requiere que categoria tenga null=True.
#models.SET_DEFAULT	Se asigna el valor por defecto al campo. Requiere que el campo tenga default=....
#models.SET(función)	Se ejecuta una función que retorna el valor a usar como reemplazo.
#models.DO_NOTHING	No hace nada. Si la base de datos no permite claves foráneas "rotas", lanza error.

#Tipos de relaciones:
#MUCHOS A UNO: ForeignKey()
#MUCHOS A MUCHOS: ManyToManyField()
#UNO A UNO: OneToOneField()

#DATOS DE UTILIDAD
#Campos para texto
#CharField(max_length=255): Usado para campos de texto corto, como nombres o títulos. max_length es obligatorio.
#TextField(): Usado para campos de texto largo, como descripciones. No requiere max_length.

#SlugField(): Similar a CharField, pero utilizado para almacenar una versión amigable para la URL de un campo (por ejemplo, un nombre o título convertido a minúsculas con guiones).

#EmailField(): Para almacenar direcciones de correo electrónico. Validación automática.

#URLField(): Para almacenar URLs. Validación automática.

#Campos para números
#IntegerField(): Para almacenar enteros (números sin decimales).

#BigIntegerField(): Similar a IntegerField, pero para números más grandes.

#PositiveIntegerField(): Almacena enteros positivos.

#PositiveSmallIntegerField(): Almacena pequeños enteros positivos.

#SmallIntegerField(): Almacena pequeños enteros, con un rango más limitado que IntegerField.

#DecimalField(max_digits=5, decimal_places=2): Para almacenar números decimales con una cantidad específica de dígitos totales y dígitos decimales.

#FloatField(): Para almacenar números de punto flotante (con decimales).

#BooleanField(): Para almacenar un valor True o False.

#NullBooleanField(): Similar a BooleanField, pero permite almacenar valores None (nulo).

#Campos de fecha y hora
#DateField(): Almacena una fecha (sin hora).

#DateTimeField(): Almacena una fecha y una hora.

#TimeField(): Almacena solo una hora.

#DurationField(): Almacena una duración de tiempo (por ejemplo, 1 día, 2 horas, 30 minutos).

#Campos relacionados con otras tablas (relaciones)
#ForeignKey(model, on_delete=models.CASCADE): Relación de "muchos a uno". Relaciona el modelo actual con otro modelo (como un campo de clave foránea).

#ManyToManyField(model): Relación de "muchos a muchos". Relaciona el modelo actual con otro modelo, permitiendo que varios registros estén relacionados con varios registros del otro modelo.

#OneToOneField(model): Relación de "uno a uno". Relaciona el modelo actual con otro modelo, asegurando que haya solo un registro relacionado.

#Otros campos especiales
#ImageField(upload_to='images/'): Para almacenar imágenes. Requiere que tengas configurado MEDIA_URL y MEDIA_ROOT en tu configuración.

#FileField(upload_to='files/'): Para almacenar archivos (no solo imágenes).

#JSONField(): Almacena datos en formato JSON (disponible desde Django 3.1).

#ArrayField(): Usado en bases de datos como PostgreSQL, almacena una lista de elementos.

#HStoreField(): Almacena un diccionario de clave-valor (disponible en PostgreSQL).

#Campos para configuraciones especiales
#AutoField(): Campo de clave primaria autoincrementable (por defecto se usa id como AutoField si no se especifica).

#UUIDField(): Almacena un identificador único universal (UUID).

#IPAddressField(): Almacena una dirección IP.

#GenericIPAddressField(): Almacena una dirección IP, soportando tanto IPv4 como IPv6.

#XMLField(): Almacena datos XML (disponible en PostgreSQL).

#Campos para valores de elección (choices)
#IntegerField(choices=CHOICES): Puedes utilizar choices para limitar los valores posibles del campo a un conjunto predefinido de valores.

#CharField(choices=CHOICES): Similar a IntegerField, pero para valores de texto predefinidos.

#Campos de tiempo
#TimeDeltaField(): Almacena diferencias de tiempo (disponible en PostgreSQL).