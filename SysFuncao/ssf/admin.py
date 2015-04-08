from django.contrib import admin
from ssf.models import Sistema, Requisicao, Mensagem
from django.contrib.admin.options import ModelAdmin

class SistemaAdmin(ModelAdmin):
    fields = ('nome', 'finalidade', 'responsavel',)
    list_display = ("nome","responsavel", 'finalidade',)
    list_filter = ('responsavel',)
    search_fields = ('nome', 'finalidade',)

class RequisicaoAdmin(ModelAdmin):
    fields = ('criador','status_tipo','sistema','dataHora', 'interessados',)
    list_display = ('sistema',"status_tipo","criador",'dataHora')
    
    list_filter = ('status_tipo','sistema',)
    date_hierarchy = 'dataHora'
    filter_horizontal = ('interessados',)

class MensagemAdmin(ModelAdmin):
    list_display = ('conteudo','usuario','dataHora')
    list_filter = ('usuario', 'requisicao_associada',)
    date_hierarchy = 'dataHora'

admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Requisicao, RequisicaoAdmin)
admin.site.register(Mensagem, MensagemAdmin)