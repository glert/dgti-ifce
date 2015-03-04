
from django.contrib import admin
from requisitador.models import Requisicao, Sistema


class SistemaAdmin(admin.ModelAdmin):
    fields = ('nome', 'finalidade', 'responsaveis')
    pass
  
class RequisicaoAdmin(admin.ModelAdmin):
    fields = ('sistema','status','descricao', 'criador', 'interessados','prioridade')
    pass


admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Requisicao, RequisicaoAdmin)

