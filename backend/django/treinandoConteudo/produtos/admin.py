from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome_categoria']
    search_fields = ['nome_categoria']
    list_per_page = 20
    
    pass

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome_produto', 'categoria', 'data_cadastro', 'codigo_produto', 'esgotado']
    search_fields = ['nome_produto', 'categoria__nome_categoria']
    list_filter = ['categoria__nome_categoria', 'esgotado']
    list_editable = ['esgotado',]
    list_per_page = 20
    
    pass