from rest_framework import viewsets
from aplicacion.serializers import UserSerializer
from aplicacion.models import User
#from rest_framework.permissions import IsAuthenticated

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
   #permission_classes = (IsAuthenticated,)