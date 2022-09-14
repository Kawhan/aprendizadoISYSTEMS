from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForm

# Create your views here.
def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForm()
    
    context = {'form': form, 'pessoa_form': pessoa_form}
    
    return render(request, 'index.html', context)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForm(request.POST)
        
        if form.is_valid() and pessoa_form.is_valid():
            context = {'form': form, 'pessoa_form': pessoa_form}
            return render(request, 'minha_consulta.html', context)
        else:
            print('Form inválido')
            context = {'form': form, 'pessoa_form': pessoa_form}

            return render(request, 'index.html', context)