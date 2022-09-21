from django.contrib import admin
from animais.models import Animal

# Register your models here.
@admin.register(Animal)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome_animal', 'venenoso']
    search_fields = ['nome_categoria']
    list_per_page = 20
    
    pass