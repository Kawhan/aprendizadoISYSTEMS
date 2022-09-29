from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

