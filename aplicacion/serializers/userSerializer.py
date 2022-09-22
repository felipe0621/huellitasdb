from rest_framework import serializers
from aplicacion.models import User
#from .productosSerializer import ProductosSerializer
#from aplicacion.models import Productos

class UserSerializer(serializers.ModelSerializer):
    #productos = ProductosSerializer()
    
    class Meta:
        model = User
        
        #fields = ['id', 'username', 'password', 'name', 'idCard', 'address', 'phone','email', 'productos']
        fields = ['id', 'username', 'name', 'idCard', 'address', 'phone','email']
        
''' 
    def create(self, validated_data):
        productosData = validated_data.pop('productos')
        userInstance = User.objects.create(**validated_data)
        Productos.objects.create(user=userInstance, **productosData)
        return userInstance
    
    def to_representation(self, obj):
      user = User.objects.get(id=obj.id)
      productos = Productos.objects.get(user=obj.id)
      return{
          'id': user.id,
          'username': user.username,
          'name': user.name,
          'idCard': user.idCard,
          'address': user.address,
          'phone': user.phone,
          'email': user.email      
          
      }         
''' 