# -*- coding:utf-8 -*-
from django import forms

from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from ssf.models import Sistema
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import RadioSelect


class NovaRequisicaoForm(forms.Form):  
    
    sistema = forms.ModelChoiceField(queryset=Sistema.objects.all())
    mensagem = forms.CharField(label="Descrição",
        max_length=1024,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Descreva a Funcionalidade',
                'maxlength':"1024",
            }
        ),
    )
    interessados = forms.ModelMultipleChoiceField(label="", queryset=User.objects.all(),                                        
                                           widget=FilteredSelectMultiple(
                                                     "Pessoas Interessadas",
                                                     is_stacked=False,
                                                     attrs={'rows':'10'},
                                                  )
                                          )  
   
    class Media:
        css = {"all":('/static/admin/css/widgets.css',),}
        js = ('/admin/jsi18n',)

class NovaMensagemForm(forms.Form):
        BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))
        mensagem = forms.CharField(
            max_length=2048,
            widget=forms.Textarea(
                attrs={
                    'placeholder': 'Escreva sua mensagem',
                    'maxlength':"2048",
                    'rows':"6",
                }
            ),
        )
        booleanEmail = forms.BooleanField(required=True, label="Enviar um email lembrete a todos:", 
                                           widget=RadioSelect(choices=[(True, 'Sim'),(False, 'Não')]))
class DocumentoReqForm(forms.Form):
    documento = forms.FileField()
          
    
