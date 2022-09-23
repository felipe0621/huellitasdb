from aplicacion.models.mediosP import MediosP
from rest_framework import serializers
from aplicacion.models import MediosP

class MediosPSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediosP
        fields = ['id','valorApagar', 'efectivo', 'tarjeta_debito', 'tarjeta_credito', 'pse','user']
        