from django.contrib import admin
from ssf.models import Sistema, Requisicao, Mensagem
from django.contrib.admin.options import ModelAdmin

class SistemaAdmin(ModelAdmin):
    fields = ('nome', 'finalidade')
    list_filter = ('nome',)


admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Requisicao)
admin.site.register(Mensagem)