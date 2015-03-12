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
                   
        #return TemplateView.get(self, request, {'form': NovaRequisicaoForm(), 'layout': layout})
        return render(request, self.template_name, {'form': NovaRequisicaoForm(), 'layout': layout})
    
    @method_decorator(login_required)
    def post(self, request):
        formul = NovaRequisicaoForm(request.POST)
        if formul.is_valid():
            print formul.cleaned_data
        else:
            print formul.errors
            
        #return TemplateView.get(self, request, {'form': formul, 'layout': 'vertical'})
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


