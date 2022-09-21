from django.db import models
from .user import User

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='productos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=80)
    cantidad = models.IntegerField(default=0)
    proveedor = models.CharField(max_length=50)
    valor = models.IntegerField(default=0)
    
    
    
