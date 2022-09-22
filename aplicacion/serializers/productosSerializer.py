from aplicacion.models.productos import Productos
from rest_framework import serializers
from aplicacion.models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id','descripcion', 'cantidad', 'proveedor', 'valor', 'user']
        #fields = ['id','descripcion', 'cantidad', 'proveedor', 'valor']
        
