from django.conf.urls import patterns, include, url
from django.contrib import admi
from django.views.generic import TemplateView
from ssf.views import LoginView, LogadoVie
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

admin.autodiscover() 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SysFuncao.views.home', name='home'),
    # url(r'^SysFuncao/', include('SysFuncao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', LoginView.as_view()),
    #url(r'^accounts/auth/$', 'ssf.views.auth_view'),
    url(r'^accounts/loggedin/$', LogadoView.as_view()),
    #url(r'^accounts/logout/$', 'ssf.views.logout'),
    #url(r'^accounts/addrequisitos/$', NovaRequisicaoView.as_view()),
    url(r'^accounts/addrequisitos/$', 'ssf.views.addrequisitos'),
    url(r'^accounts/consultarrequisicao/$', 'ssf.views.consultarrequisicao'),
    #url(r'^form$', 'ssf.views.form'),
    # acao do botao sair
      
    
)
