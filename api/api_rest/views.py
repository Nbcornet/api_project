from rest_framework import viewsets
from api.models import Producto
from api.api_rest.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    print(queryset)
    serializer_class = ProductoSerializer

    