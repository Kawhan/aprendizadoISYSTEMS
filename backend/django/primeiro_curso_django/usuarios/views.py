from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        # Validando se o nome é null
        if not nome.strip():
            print("O nome não pode ficar em branco")
            return redirect('cadastro')
        
        # Validando se o campo de email não esta em branco
        if not nome.strip():
            print("O campo email não pode ficar em branco")
            return redirect('cadastro')
            
        # Validando senha
        if senha != senha2:
            print("As senhas não são iguais!")
            return redirect('cadastro')
        
        # Verificar se o usuário que queremos criar está na base de dados
        if User.objects.filter(email=email).exists():
            print("Usuario já cadastrado")
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        
        user.save()
        print("Usuário cadastrado com sucesso!")
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if not email.strip():
            print("O campo email não pode ficar em branco")
            return redirect('login')
        
        if not senha.strip():
            print("Senha vazia!")
            return redirect('login')
        
        
        # Trazendo as informações desse usuário apartir do email
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            
            user = auth.authenticate(request, username=nome, password=senha)
            
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso!")
                return redirect('dashboard')
            
    else:
        return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')