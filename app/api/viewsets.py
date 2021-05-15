from rest_framework import viewsets
from app import models
from app.api import serializers


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriaSerializer
    queryset = models.Categoria.objects.all()

class ImovelViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ImovelSerializer
    queryset = models.Imovel.objects.all()

class VendaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VendaSerializer
    queryset = models.Venda.objects.all()    