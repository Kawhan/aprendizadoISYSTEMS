from rest_framework import viewsets
from escola.models import AlunoModel, CursoModel
from .serializer import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = AlunoModel.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = CursoModel.objects.all()
    serializer_class = CursoSerializer