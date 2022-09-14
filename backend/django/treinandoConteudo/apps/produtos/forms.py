from gc import disable
from django import forms
from .models import Categoria, Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        
        fields = [
            "nome_produto",
            "validade",
            "codigo_produto",
            "valor",
            "quantidade_estoque",
            "descricao",
            "categoria",
            "esgotado"
        ]
        
        labels = {
            'descricao' : 'Descrição do produto',
            'codigo_produto' : 'Código produto'
        }
        
        

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        
        fields = [
            "nome_categoria"
        ]
        
       