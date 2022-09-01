from pydoc import plain
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categoria, Produto
from .forms import ProdutoForm, CategoriaForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def index(request):
    return render(request,'index.html')


def listarProdutos(request):
    produtos = Produto.objects.filter(esgotado=False)
    
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
    
    return render(request, 'view-produto.html', dados)

@login_required
def create_produto(request):
    context  = {}
        
    form = ProdutoForm(request.POST or None)
        
    if form.is_valid():
        form.save()
        return redirect('/produtos')
        
    context['form']= form
 
    return render(request, 'create_produto.html', context) 

@login_required
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

@user_passes_test(lambda u: u.is_superuser)
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
@login_required
def create_categoria(request):
    context = {}
    
    form = CategoriaForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('/categoria')
    
    context["form"] = form
    
    return render(request, "create_categoria.html", context)

@login_required
def change_categoria(request, categoria_id):
    context ={}
    categoria = get_object_or_404(Categoria, pk=categoria_id) 
    
    form = CategoriaForm(request.POST or None, instance= categoria)
    
    if form.is_valid():
        # print(form.id)
        form.save()
        return redirect('/categoria')
    
    context["form"] = form
 
    return render(request, "update_view_categoria.html", context)
    
@user_passes_test(lambda u: u.is_superuser)
def delete_categoria(request, categoria_id):
    context ={}
    categoria = get_object_or_404(Categoria, pk=categoria_id) 
    
    context['categoria'] = categoria
    
    if request.method =="POST":
        # delete object
        categoria.delete()
        # after deleting redirect to
        # home page
        return redirect("/categoria")
 
    return render(request, "delete_view_categoria.html", context)

def view_categoria(request, categoria_id):
    context = {}
    
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    
    context['categoria'] = categoria
    
    return render(request, 'view_categoria.html', context)

def search(request):
    produtos = Produto.objects.filter(esgotado=False)
    
    if 'search' in request.GET:
        search_name = request.GET['search']
        if search_name:
            produtos = produtos.filter(nome_produto__icontains=search_name)
    
    dados = {
        'produtos': produtos
    }
    
    return render(request,'search.html', dados)