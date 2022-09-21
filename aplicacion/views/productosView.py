from rest_framework import viewsets
from aplicacion.serializers import ProductosSerializer
from aplicacion.models import Productos
#from rest_framework.permissions import IsAuthenticated

class ProductosView(viewsets.ModelViewSet):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()
   #permission_classes = (IsAuthenticated,)