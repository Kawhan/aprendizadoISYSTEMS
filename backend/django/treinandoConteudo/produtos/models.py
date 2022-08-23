from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome_categoria

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto + ' - ' + str(self.categoria)

    
    