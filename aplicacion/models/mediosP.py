from django.db import models
from .user import User

class MediosP(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='mediosP', on_delete=models.CASCADE)
    valorApagar = models.IntegerField( )
    efectivo = models.BooleanField(default=True)
    tarjeta_debito = models.BooleanField(default=False)
    tarjeta_credito = models.BooleanField(default=False)
    pse =  models.BooleanField(default=False)
    