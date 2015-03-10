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
    template_name = "login.html"
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
    template_name = "loggedin.html"
    
    @method_decorator(login_required)
    def get(self, request):
        return TemplateView.get(self, request, {'full_name': request.user.username})
    
    
class NovaRequisicaoView(TemplateView):
    template_name = "addrequisitos.html"
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        kwargs.append('form', NovaRequisicaoForm())
        return TemplateView.get(self, request, *args, **kwargs)
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = NovaRequisicaoForm(request.POST)
        print form
            

@login_required
def addrequisitos(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = NovaRequisicaoForm(request.POST)
         
        if form.is_valid():
            
            return HttpResponseRedirect('/accounts/loggedin')
            
    else:
        form = NovaRequisicaoForm()
#    form.fields['title'].widget = BootstrapUneditableInput()
    return render_to_response('addrequisitos.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))


