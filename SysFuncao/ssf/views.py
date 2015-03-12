# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from django.template import RequestContext

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ssf.forms import *
from datetime import datetime
from ssf.models import Requisicao, Mensagem


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
        return render(request, self.template_name, {'full_name': request.user.username})
    
    
class NovaRequisicaoView(TemplateView):
    template_name = "addrequisitos.djhtml"
    
    @method_decorator(login_required)
    def get(self, request):
        layout  = request.GET.get('layout', None)
        if layout == None:
            layout = 'vertical'
       
        return render(request, self.template_name, {'form': NovaRequisicaoForm(), 'layout': layout})
    
    @method_decorator(login_required)
    def post(self, request):
        formul = NovaRequisicaoForm(request.POST)
        if formul.is_valid():
            nomeSistema = formul.cleaned_data['sistema']
            interessados = formul.cleaned_data['interessados']
            msg_form = formul.cleaned_data['mensagem']
            criador = request.user
#                    
#             interessadosObjs = []
#             for nome_u in interessados:
#                 interessadosObjs.append(User.objects.get_by_natural_key(nome_u))            
            
            
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
              
        else:
            print formul.errors
            
        return render(request, self.template_name, {'form': NovaRequisicaoForm(), 'layout': 'vertical'})    

@login_required
def addrequisitos(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = NovaRequisicaoForm(request.POST)
         
        if form.is_valid():
            #tem que introduzir algo na persistência
            return HttpResponseRedirect('/accounts/loggedin')
            
    else:
        form = NovaRequisicaoForm()
#    form.fields['title'].widget = BootstrapUneditableInput()
    return render_to_response('addrequisitos.djhtml', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))


