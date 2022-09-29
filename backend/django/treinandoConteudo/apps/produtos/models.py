from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome_categoria

class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    validade = models.IntegerField()
    codigo_produto = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    descricao = models.TextField()
    esgotado = models.BooleanField(default=False)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome_produto + ' - ' + str(self.categoria)

    
    