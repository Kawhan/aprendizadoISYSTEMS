from rest_framework import viewsets
from escola.models import AlunoModel, CursoModel, MatriculaModel
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = AlunoModel.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = CursoModel.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """ Listando todas as matriculas """
    queryset = MatriculaModel.objects.all()
    serializer_class = MatriculaSerializer