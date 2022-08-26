import re
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categoria, Produto
from .forms import ProdutoForm, CategoriaForm

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

def informacao(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id) 
    
    dados  = {
        'produto': produto
    }
    
    return render(request, 'informacoesProduto.html', dados)

def create_produto(request):
    context  = {}
        
    form = ProdutoForm(request.POST or None)
        
    if form.is_valid():
        form.save()
        return redirect('/produtos')
        
    context['form']= form
 
    return render(request, 'create_produto.html', context) 

def change_produto(request, produto_id):
    context ={}
    produto = get_object_or_404(Produto, pk=produto_id) 
    
    form = ProdutoForm(request.POST or None, instance= produto)
    
    if form.is_valid():
        # print(form.id)
        form.save()
        return redirect('/produtos')
    
    context["form"] = form
 
    return render(request, "update_view.html", context)

def delete_produto(request, produto_id):
    context ={}
    produto = get_object_or_404(Produto, pk=produto_id) 
    
    context['produto'] = produto
    
    if request.method =="POST":
        # delete object
        produto.delete()
        # after deleting redirect to
        # home page
        return redirect("/produtos")
 
    return render(request, "delete_view.html", context)

# Categoria CRUD

def create_categoria(request):
    context = {}
    
    form = CategoriaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('/categoria')
    
    context["form"] = form
    
    return render(request, "create_categoria.html", context)
    