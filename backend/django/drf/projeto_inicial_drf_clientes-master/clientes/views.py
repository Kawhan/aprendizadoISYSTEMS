from warnings import filters
from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter ]
    ordering_fields    = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']

