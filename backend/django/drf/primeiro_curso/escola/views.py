from rest_framework import viewsets, generics
from escola.models import AlunoModel, CursoModel, MatriculaModel
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer

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

class ListaMatriculasAluno(generics.ListAPIView):
    """ Listando as matriculas de um aluno ou aluna """
    def get_queryset(self):
        queryset = MatriculaModel.objects.filter(aluno_id =self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer