from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Produto

# Create your views here.
def index(request):
    return render(request,'index.html')


def listarProdutos(request):
    produtos = Produto.objects.all()
    
    dados = {
        'produtos': produtos
    }
    
    return render(request,'listarProdutos.html', dados)

def listarCategoria(request):
    categorias = Categoria.objects.all()
    
    dados = {
        'categorias': categorias
    }
    
    return render(request, 'listarCategoria.html', dados)
