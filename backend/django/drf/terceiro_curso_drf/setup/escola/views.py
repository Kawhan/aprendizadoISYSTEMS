from escola.models import Aluno, Curso, Matricula
from escola.serializer import (AlunoSerializer, AlunoSerializerV2,
                               CursoSerializer,
                               ListAlunosMatriculadosCursoSerializer,
                               ListaMatriculasAlunoSerializer,
                               MatriculaSerializer)
from rest_framework import generics, status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = Aluno.objects.all()
    authentication_classes = [BasicAuthentication]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response


class MatriculaViewSet(viewsets.ModelViewSet):
    """ Exibindo todas as matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]


class ListaMatriculasAluno(generics.ListAPIView):
    """ Listando as matriculas de um aluno """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]


class ListaAlunosMatriculados(generics.ListAPIView):
    """ Listando alunos e alunas matriculados em um curso """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListAlunosMatriculadosCursoSerializer
    authentication_classes = [BasicAuthentication]
