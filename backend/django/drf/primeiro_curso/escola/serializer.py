from pyexpat import model
from rest_framework import serializers
from escola.models import AlunoModel, CursoModel

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoModel
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoModel
        fields = '__all__'