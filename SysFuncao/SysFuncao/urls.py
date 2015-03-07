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
   # url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^accounts/auth/$', 'ssf.views.auth_view'),
    url(r'^accounts/logout/$', 'ssf.views.logout', name="home"),
    url(r'^accounts/loggedin/$', 'ssf.views.loggedin'),
    url(r'^accounts/invalid/$', 'ssf.views.invalid_login'),
    
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^form$', 'ssf.views.demo_form'),
    url(r'^form_template$', 'ssf.views.demo_form_with_template'),
    url(r'^form_inline$', 'ssf.views.demo_form_inline'),
    url(r'^formset$', 'ssf.views.demo_formset', {}, "formset"),
    url(r'^tabs$', 'ssf.views.demo_tabs', {}, "tabs"),
    url(r'^pagination$', 'ssf.views.demo_pagination', {}, "pagination"),
    url(r'^widgets$', 'ssf.views.demo_widgets', {}, "widgets"),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
      
    
)
