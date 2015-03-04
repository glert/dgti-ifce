from django.conf.urls import patterns, include, url
from django.contrib import admin 
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
)
