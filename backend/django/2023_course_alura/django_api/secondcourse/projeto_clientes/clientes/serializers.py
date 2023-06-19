from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *
from clientes.validators import Validators

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        for k, v in Validators.validators_data.items():
            if v(data) != data:
                raise serializers.ValidationError(v(data))
        
        return data