from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import *
from passagens.validation import *

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label="Ida", widget=DatePicker())
    data_volta = forms.DateField(label="Volta", widget=DatePicker())
    data_pesquisa = forms.DateField(label="Data da Pesquisa", disabled=True, initial=datetime.today())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipo_de_classes)
    informacoes = forms.CharField(
        label="Informações extras",
        max_length=200,
        widget=forms.Textarea(),
        required=False,
    )
    email = forms.EmailField(label="Email", max_length=150)
     
    def clean(self):
        origem = self.cleaned_data.get("origem")
        destino = self.cleaned_data.get("destino")
        lista_de_erros = {}
        
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_error = lista_de_erros[erro]
                self.add_error(erro, mensagem_error)
                
        return self.cleaned_data