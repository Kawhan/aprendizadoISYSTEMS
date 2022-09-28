from rest_framework import serializers
from produtos.models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    # categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), many=False)
    # categoria = serializers.SerializerMethodField('get_categoria')
    
    
    class Meta:
        model = Produto
        fields = ['id','nome_produto', 'validade', 'codigo_produto', 'valor', 'quantidade_estoque', 'descricao', 'esgotado', 'categoria']

 