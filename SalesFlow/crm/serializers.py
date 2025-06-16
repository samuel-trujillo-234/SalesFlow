from rest_framework import serializers
from .models import Cliente, Tarea, Venta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
