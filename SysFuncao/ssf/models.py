#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
 
class Sistema(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    finalidade = models.TextField()
    Responsavel = User
    def __unicode__(self):
        return self.nome
    
class Requisitacao2(models.Model):
    sistema = models.ForeignKey(Sistema)
    descricao = models.TextField()   
    responsavel = models.TextField()
    
    def __unicode__(self):
        return self.descricao, self.sistema
    
class Requisicao(models.Model):  
    
    _STATUSES_TYPE = (
        (u'novo', u'Novo'),
        (u'analise de viabilidade', u'Análise de viabilidade'),
        (u'viavel', u'Viável'),
        (u'em implementacao', u'Em implementação'),
        (u'rejeitado', u'Rejeitado'),
        (u'finalizado e operacional', u'Finalizado e operacional'),
    )    
    sistema = models.ForeignKey(Sistema)    
    status_tipo = models.CharField(max_length=64, choices=_STATUSES_TYPE, verbose_name='Status')
    criador = models.ForeignKey(User, related_name='criador', null=False, blank=False)
    
    
    interessados = models.ManyToManyField(User, related_name='interessados')
    
    @staticmethod
    def getStatusNovo():
        for optgroup_key, optgroup_value in Requisicao._STATUSES_TYPE:
            if('novo' ==  optgroup_key):
                return optgroup_value 
                #return self._STATUSES_TYPE[0][0]
    
        
    def __unicode__(self):
        return "(%s) %s por %s" % (self.pk, Sistema.objects.get(pk=self.sistema), User.objects.get(pk =self.criador))

class Mensagem(models.Model):
    dataHora = models.DateTimeField()
    conteudo = models.TextField();
    usuario = models.ForeignKey(User)    
    requisicao_associada = models.ForeignKey(Requisicao)
    def __unicode__(self):
        result = str(self.conteudo)
        if result.len() >= 20:
            result = '%s...' % result[:18]            
        return result 
          
    