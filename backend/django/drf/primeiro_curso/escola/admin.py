from django.contrib import admin
from escola.models import AlunoModel, CursoModel


# Register your models here.
@admin.register(AlunoModel)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
    search_fields = ['nome', 'rpg', 'cpf', 'data_nascimento']
    list_display_links = ['id', 'nome']
    list_filter = ['data_nascimento',]
    list_per_page = 20
    
    pass

@admin.register(CursoModel)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo_curso', 'descricao', 'nivel']
    list_display_links = ['id', 'codigo_curso',]
    search_fields = ['codigo_curso',]    
    list_filter = ['nivel',]
    list_per_page = 20
    
    pass