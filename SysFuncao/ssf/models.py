#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
 
class Sistema(models.Model):
    nome = models.CharField(max_length=64, unique=True)
    finalidade = models.TextField()
    Responsavel = User
    def __unicode__(self):
        return u"%s" % self.nome
    
class Requisicao(models.Model):  
    
    _STATUSES_TYPE = (
        (u'novo', u'Novo'),
        (u'analise de viabilidade', u'Análise de viabilidade'),
        (u'viavel', u'Viável'),
        (u'em implementacao', u'Em implementação'),
        (u'rejeitado', u'Rejeitado'),
        (u'finalizado e operacional', u'Finalizado e operacional'),
    )    
    sistema = models.ForeignKey(Sistema, null=False, blank=False)    
    status_tipo = models.CharField(max_length=64, choices=_STATUSES_TYPE, verbose_name='Status')
    criador = models.ForeignKey(User, related_name='criador', null=False, blank=False)  
    interessados = models.ManyToManyField(User, related_name='interessados')
    
    @staticmethod
    def getStatusNovo():
        StatusNovo = Requisicao.status_tipo = 'novo'
        return StatusNovo    
#         for optgroup_key, optgroup_value in Requisicao._STATUSES_TYPE:
#             if('novo' ==  optgroup_key):
#                 return optgroup_value 
    def getLastMessage(self):
        maiorData = self.mensagem_set.all().aggregate(Max('dataHora'))['dataHora__max']
        return self.mensagem_set.get(dataHora=maiorData)
    
        
    def __unicode__(self): 
        return u'%s %s %s' % (self.pk, self.sistema, self.criador)

class Mensagem(models.Model):
    dataHora = models.DateTimeField(null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    usuario = models.ForeignKey(User, null=False, blank=False)    
    requisicao_associada = models.ForeignKey(Requisicao)
    
    def __unicode__(self):
        result = unicode(self.conteudo)
        if len(result) >= 20:
            result = u'%s...' % result[:18]            
        return result 
          
    