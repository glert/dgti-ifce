from django.conf.urls import patterns, include, url
from django.contrib import admin 
from django.views.generic import TemplateView

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
    
    url(r'^$', 'ssf.views.login'),
    url(r'^accounts/auth/$', 'ssf.views.auth_view'),
    url(r'^accounts/loggedin/$', 'ssf.views.loggedin'),
    url(r'^$', 'ssf.views.logout'),
    url(r'^accounts/addrequisitos/$', 'ssf.views.addrequisitos'),
   
    
    # acao do botao sair
      
    
)
