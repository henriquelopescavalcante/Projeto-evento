from django.contrib import admin

from eventos.models import Inscricao, Evento, Categoria


@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    
    list_display = ['nome', 'email', 'interesse', 'data']
    search_fields = ['nome', 'email']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'criado_em', 'modificado_em']
    search_fields = ['nome']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'categoria', 'data', 'destaque', 'criado_em', 'modificado_em']
    search_fields = ['nome', 'categoria__nome']
