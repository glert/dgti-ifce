#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

class des2(models.Model):
    descricao = models.TextField()
    
    def __unicode__(self):
        return self.descricao
 
class Sistema(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    finalidade = models.TextField()
    Responsavel = User
    def __unicode__(self):
        return self.nome
 

class Requisicao(models.Model):  
    STATUSES_TYPE = (
        (u'novo', u'Novo'),
        (u'análise de viabilidade', u'Análise de viabilidade'),
        (u'viável', u'Viável'),
        (u'em implementação', u'Em implementação'),
        (u'rejeitado', u'Rejeitado'),
        (u'finalizado e operacional', u'Finalizado e operacional'),
    )    
    sistema = models.ForeignKey(Sistema)    
    status_tipo = models.CharField(max_length=15, choices=STATUSES_TYPE, verbose_name='Status')
    criador = models.ForeignKey(User, related_name='criador', null=False, blank=False)
    
    
    interessados = models.ManyToManyField(User, related_name='interessados')
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
          
    