from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UsersMetaData (models.Model) :
    user = models.ForeignKey(User, models.DO_NOTHING) #A los usuarios le spodes poner lo que quieras pero si o si deben tener este atributo que es de la base de datos de usuarios de django
    token = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_user} {self.last_name}" #SON EL USUARIO Y SU APAELLIDO
    
    class Meta :
        db_table = 'users_metadata'
        verbose_name = 'User_Metadata'
        verbose_name_plural = 'Users_Metadata'