from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_validado(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF invalido!"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Você não deve colocar números no nome!"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 digitos!"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: opcional(+55) obrigatorio(8399999-9999)"})   
        return data
    
    
    
            