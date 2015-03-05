#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User       
 
class Sistema(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    finalidade = models.TextField()
 
    def __unicode__(self):
        return self.nome
 
class Requisito(models.Model):  
    STATUSES_TYPE = (
        (u'novo', u'Novo'),
        (u'análise de viabilidade', u'Análise de viabilidade'),
        (u'viável', u'Viável'),
        (u'em implementação', u'Em implementação'),
        (u'rejeitado', u'Rejeitado'),
        (u'finalizado e operacional', u'Finalizado e operacional'),
    )
    status_id = models.AutoField(primary_key=True)
    sistema = models.ForeignKey(Sistema)
    status_tipo = models.CharField(max_length=15, choices=STATUSES_TYPE, verbose_name='Status')
    status_descricao = models.TextField(verbose_name='Descricao')
    def __unicode__(self):
        return self.status_descricao
      
    