from django.db import models

# Create your models here.
class AlunoModel(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Aluno'
    

class CursoModel(models.Model):
    nivel = (
        ("B", 'Básicos'),
        ('I', 'Intermediário'),
        ("A", 'Avançado')
    )
    
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=nivel, blank=False, null=False, default='B')
    
    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = 'Curso'