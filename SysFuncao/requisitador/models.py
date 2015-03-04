#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
# class Usuario(User):
#     nome = models.CharField(max_length=128)
#     login = models.CharField(max_length = 64)
#     email = models.EmailField(unique=True)
#     senha = models.CharField(max_length =64)
#     
class Casa(models.Model):
    endereco = models.CharField(max_length=128)
    cep = models.CharField(max_length=8)
    def __unicode__(self):
        return self.cep
          
 
class Sistema(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    finalidade = models.TextField()
    responsaveis = models.ManyToManyField(User)
    def __unicode__(self):
        return self.nome
 
class Requisicao(models.Model):
    STATUSES_TYPE = (
        ('N', 'Novo'),
        ('A', 'Análise de viabilidade'),
        ('V','Viável'),
        ('I', 'Em implementação'),
        ('R','Rejeitado'),
        ('F','Finalizado e operacional'),
    )
    PRIORITY_TYPE = (
        ('B','Baixa'),
        ('N','Normal'),
        ('A','Alta'),
        ('M', 'Máxima'),
    )
    sistema = models.ForeignKey(Sistema)
    status = models.CharField(max_length=1, choices=STATUSES_TYPE)
    descricao = models.TextField()
    criador = models.ForeignKey(User, related_name ='criador')
    interessados = models.ManyToManyField(User, related_name='interessados')
    prioridade = models.CharField(max_length=1, choices= PRIORITY_TYPE)
     
    def __unicode__(self):
        self.descricao 
     
     
