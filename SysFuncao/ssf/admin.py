from django.contrib import admin
from ssf.models import Sistema, Requisicao, Mensagem
from django.contrib.admin.options import ModelAdmin

class SistemaAdmin(ModelAdmin):
    fields = ('nome', 'finalidade', 'responsavel')
    list_filter = ('nome',)

class RequisicaoAdmin(ModelAdmin):
    fields = ('criador','status_tipo','sistema','dataHora')
    list_filter = ('status_tipo','sistema',)
    date_hierarchy = 'dataHora'

admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Requisicao, RequisicaoAdmin)
admin.site.register(Mensagem)