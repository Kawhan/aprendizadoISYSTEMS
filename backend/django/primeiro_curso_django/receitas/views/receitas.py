from django.shortcuts import render, get_object_or_404, redirect
from receitas.models import Receita
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_per_page = paginator.get_page(page)
    
    dados =  {
        'receitas': receitas_per_page
    }
    
    return render(request,'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita_a_exibir = {
        'receita': receita
    }
    
    return render(request,'receitas/receita.html', receita_a_exibir)



def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita.delete()
    
    messages.success(request, "Receita deletada com sucesso")
    
    return redirect("dashboard")

def edita_receita(request, receita_id):
    receita  = get_object_or_404(Receita, pk=receita_id)
    
    receita_a_editar = {}
    
    receita_a_editar['receita'] =  receita
    
    return render(request, 'receitas/editar_receita.html', receita_a_editar)

def atualiza_receita(request):
    if request.method == "POST":
        receita_id = request.POST['receita_id']
        
        receita_antiga = Receita.objects.get(pk=receita_id)
        
        receita_antiga.nome_receita = request.POST['nome_receita']
        receita_antiga.ingredientes = request.POST['ingredientes']
        receita_antiga.modo_preparo = request.POST['modo_preparo']
        receita_antiga.tempo_preparo = request.POST['tempo_preparo']
        receita_antiga.rendimento = request.POST['rendimento']
        receita_antiga.categoria = request.POST['categoria']
        
        if 'foto_receita' in request.FILES:
            receita_antiga.foto_receita = request.FILES['foto_receita']
        
        receita_antiga.save()
        
        
        return redirect('dashboard')
    
def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        
        user  = get_object_or_404(User, pk=request.user.id)
        nova_receita = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento, categoria=categoria, foto_receita=foto_receita)
        
        nova_receita.save()
        
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')
        
        