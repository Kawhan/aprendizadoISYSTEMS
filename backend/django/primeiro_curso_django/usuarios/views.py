from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        # Validando se o nome é null
        if Verificacao.campo_vazio(nome):
            messages.error(request,"O nome não pode ficar em branco")
            return redirect('cadastro')
        
        # Validando se o campo de email não esta em branco
        if Verificacao.campo_vazio(email):
            messages.error(request, "O campo email não pode ficar em branco")
            return redirect('cadastro')
            
        # Validando senha
        if Verificacao.senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, "As senhas não são iguais!")
            return redirect('cadastro')
        
        # Verificar se o usuário que queremos criar está na base de dados
        if User.objects.filter(email=email).exists():
            messages.error(request, "Usuario já cadastrado")
            return redirect('cadastro')
        
        if User.objects.filter(username=nome).exists():
            messages.error(request, "Usuario já cadastrado")
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        
        user.save()
        messages.success(request, "Cadastro realizado com sucesso!")
        print("Usuário cadastrado com sucesso!")
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if Verificacao.campo_vazio(email):
            messages.error(request, "O campo email não pode ficar em branco")
            return redirect('login')
        
        if Verificacao.campo_vazio(senha):
            messages.error(request, "Senha vazia!")
            return redirect('login')
        
        
        # Trazendo as informações desse usuário apartir do email
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                messages.success(request,"Login realizado com sucesso!")
                return redirect('dashboard')
            
    else:
        return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        
        dados = {}
        
        dados['receitas'] = receitas
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
    
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
        return render(request, 'usuarios/cria_receita.html')
    
def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    receita.delete()
    
    messages.success(request, "Receita deletada com sucesso")
    
    return redirect("dashboard")

class Verificacao:
    def campo_vazio(campo):
        return not campo.strip()
    
    def senhas_nao_sao_iguais(senha, senha2):
        return senha != senha2