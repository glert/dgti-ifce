# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.formtools.tests.forms import TestForm
from django.template import RequestContext

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
    
    

def form(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = TestForm(request.POST)
        form.is_valid()
    else:
        form = TestForm()
    form.fields['title'].widget = BootstrapUneditableInput()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))


