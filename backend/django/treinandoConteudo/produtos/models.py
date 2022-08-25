from django.db import models
from datetime import datetime

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome_categoria

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    validade = models.IntegerField()
    codigo_produto = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    descricao = models.TextField()
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nome_produto + ' - ' + str(self.categoria)

    
    