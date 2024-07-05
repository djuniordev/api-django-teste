from django.contrib import admin
from api.models import Aluno, Trilha

# Register your models here.
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf',)
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Trilhas(admin.ModelAdmin):
    list_display = ('id', 'tipo',)
    list_display_links = ('id', 'tipo')
    search_fields = ('tipo',)

admin.site.register(Trilha, Trilhas)