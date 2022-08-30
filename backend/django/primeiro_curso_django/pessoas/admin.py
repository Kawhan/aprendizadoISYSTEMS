from django.contrib import admin
from .models import Pessoa

# Register your models here.
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    
    list_per_page = 2
    
admin.site.register(Pessoa, PessoaAdmin)