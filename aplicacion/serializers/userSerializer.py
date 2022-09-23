from aplicacion.models.user import User
from rest_framework import serializers
from aplicacion.models import User
class UserSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User        
        fields = ['id', 'username', 'password', 'name', 'idCard', 'address', 'phone','email']
