# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from django.template import RequestContext

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from datetime import datetime
from ssf.models import Requisicao, Mensagem, Sistema
from ssf.forms import NovaRequisicaoForm
from django.contrib.auth.models import User


class LoginView(TemplateView):
    template_name = "login.djhtml"
    error = ""
    def get(self, request, ):
        deslogar = request.GET.get('logout',None)
        if deslogar is not None:        
            auth.logout(request)
        return render(request, self.template_name, csrf(request))
    def post(self, request):
        form = request.POST
        username = form['username']
        password = form['password']
        user = auth.authenticate(username=username, password=password)  
        if user is not None:            
            if user.is_active:
                auth.login(request, user)
                
                return HttpResponseRedirect('/accounts/loggedin')
            else:
                self.error = "Seu acesso ao sistema foi bloqueado, consulte o administrador"
                return render(request, self.template_name, {'error':self.error})
        else:
            self.error = "Nome de usuário e/ou senha incorretos"
            return render(request, self.template_name,{'error':self.error})
            
          
        
class LogadoView(TemplateView):
    template_name = "loggedin.djhtml"
    
    @method_decorator(login_required)
    def get(self, request):
        
        requisicoes = Requisicao.objects.filter(
                                            Q(criador=request.user) |
                                            Q(interessados__username=request.user) |
                                            Q(sistema__responsavel=request.user)
        ).distinct()
        dados = {}
        for r in requisicoes:
            dados[r] = r.getLastMessage()
        return render(request, self.template_name, {'requisicoes':dados, 'full_name': request.user.username})
    
    
    
class NovaRequisicaoView(TemplateView):
    template_name = "addrequisitos.djhtml"
    
    @method_decorator(login_required)
    def get(self, request):
        layout  = request.GET.get('layout', None)
        if layout == None:
            layout = 'vertical'
       
        return render(request, self.template_name, {'form': NovaRequisicaoForm(), 'layout': layout, 'full_name': request.user.username})
    
    @method_decorator(login_required)
    def post(self, request):
        layout = request.GET.get('layout')
        if not layout:
            layout = 'vertical'
        formul = NovaRequisicaoForm(request.POST)
        if formul.is_valid():
            nomeSistema = formul.cleaned_data['sistema']
            interessados = formul.cleaned_data['interessados']
            msg_form = formul.cleaned_data['mensagem']
            criador = request.user
#             
            novaReq = Requisicao()
            novaReq.criador = criador
            novaReq.status_tipo = Requisicao.getStatusNovo()
            novaReq.sistema = Sistema.objects.get(nome=nomeSistema)
            
            novaReq.save()           
            novaReq.interessados = interessados
            novaReq.save()
            
            msgInicial = Mensagem()
            msgInicial.usuario = request.user
            msgInicial.requisicao_associada = novaReq
            msgInicial.conteudo = msg_form
            msgInicial.dataHora = datetime.now()
            
           
            msgInicial.save()
            return HttpResponseRedirect('/accounts/loggedin')
              
        else:
            return render_to_response('addrequisitos.djhtml', RequestContext(request, {
                'form': formul,
                'layout': layout,
                }))

def dialogo(request):
    requisicoes = Requisicao.objects.filter(Q(criador=request.user) |
                                            Q(interessados__in=request.user)).distinct()
    dados = {}
    for r in requisicoes:
        dados[r] = r.getLastMessage()
    return render_to_response('dialogo.djhtml', {'requisicoes':requisicoes, 'full_name': request.user.username})

class RequisicaoView(TemplateView):
    template_name = 'dialogo.djhtml'
    
    @method_decorator(login_required) #TODO tem que colocar uma permissão aqui de acordo com o usuário
    def get(self, request, requisicao_id):
        
        requisicao = Requisicao.objects.get(pk=requisicao_id)
        mensagens = requisicao.mensagem_set.all().order_by('dataHora')
        usuarios_pk = requisicao.mensagem_set.all().values("usuario").distinct()
        usuarios = []
        for pk in usuarios_pk:
            usuarios.append(User.objects.get(pk=pk['usuario']).username)
        
        return render(request, 'dialogo.djhtml', 
                      {'mensagens': mensagens,
                       'requisicao':requisicao,
                       'full_name': request.user.username,
                       'usuarios_falantes' : usuarios, 
                       })


   