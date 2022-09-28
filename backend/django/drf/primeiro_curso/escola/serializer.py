from pyexpat import model
from rest_framework import serializers
from escola.models import AlunoModel, CursoModel, MatriculaModel

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoModel
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoModel
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaModel
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
   

    class Meta:
        model =  MatriculaModel
        fields = ['curso', 'periodo', ]
    def get_periodo(self, obj):
        return obj.get_periodo_display()