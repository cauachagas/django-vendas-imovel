from rest_framework import serializers
from app import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = "__all__"

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imovel
        fields = "__all__"

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venda
        fields = "__all__"