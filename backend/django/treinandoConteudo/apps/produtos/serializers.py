from rest_framework import serializers
from produtos.models import Categoria, Produto
from produtos.validators import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    # categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), many=False)
    # categoria = CategoriaSerializer()
    # categoria = serializers.(source='categoria.nome_categoria')
    class Meta:
        model = Produto
        fields = ['id','nome_produto', 'validade', 'codigo_produto', 'valor', 'quantidade_estoque', 'descricao', 'esgotado', 'categoria']
    
    def validate(self, data):
        if not validate_name_product(data['nome_produto']):
            raise serializers.ValidationError({"nome_produto":"Nome do produto não pode conter números"})
        if not validate_len_code_product(data['codigo_produto']):
            raise serializers.ValidationError({"codigo_produto":"Codigo do produto invalido, verifique se possui pelo menos 8 caracteres."})
        if not validade_value_product(data['valor']):
            raise serializers.ValidationError({"valor":"Valor invalido"})
        if not validade_value_product(data['quantidade_estoque']):
            raise serializers.ValidationError({"quantidade_estoque":"Quantidade de estoque invalida"})
        if not validade_validate_product(data['validade']):
            raise serializers.ValidationError({"validade":"Validade do produto incorreta"})
        return data
 