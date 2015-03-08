# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from django.contrib import messages
from django.forms.formsets import formset_factory
from django.template.context import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ssf.forms import *
from bootstrap_toolkit.widgets import BootstrapUneditableInput

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        sms = 1
        return render_to_response('login.html', {'sms': sms}, context_instance=RequestContext(request))
    
def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})


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


