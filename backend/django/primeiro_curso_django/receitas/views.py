from django.shortcuts import render
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.all()
    
    dados =  {
        'receitas': receitas
    }
    
    return render(request,'index.html', dados)

def receita(request):
    return render(request,'receita.html')