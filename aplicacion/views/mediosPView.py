from rest_framework import viewsets
from aplicacion.serializers import MediosPSerializer
from aplicacion.models import MediosP
#from rest_framework.permissions import IsAuthenticated

class MediosPView(viewsets.ModelViewSet):
    serializer_class = MediosPSerializer
    queryset = MediosP.objects.all()
   #permission_classes = (IsAuthenticated,)