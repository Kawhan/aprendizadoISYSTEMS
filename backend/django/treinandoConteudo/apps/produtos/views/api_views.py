from rest_framework import viewsets
from produtos.serializers import CategoriaSerializer, ProdutoSerializer
from produtos.models import Produto, Categoria
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(viewsets.ModelViewSet):
    """ Exibir todas as categorias  """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ProdutoViewSet(viewsets.ModelViewSet):
    """ Exibir todas os produtos mesmo sendo esgotados """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]