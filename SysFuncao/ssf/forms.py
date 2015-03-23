# -*- coding:utf-8 -*-
from django import forms

from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from ssf.models import Sistema
from django.contrib.auth.models import User
from django.contrib.admin.widgets import FilteredSelectMultiple


class TestForm(forms.Form):
    date = forms.DateField(
        widget=BootstrapDateInput(),
    )
    title = forms.CharField(
        max_length=100,
        help_text=u'This is the standard text input',
    )
    body = forms.CharField(
        max_length=100,
        help_text=u'This is a text area',
        widget=forms.Textarea(
            attrs={
                'title': 'I am "nice"',
            }
        ),
    )
    disabled = forms.CharField(
        max_length=100,
        required=False,
        help_text=u'I am disabled',
        widget=forms.TextInput(attrs={
            'disabled': 'disabled',
            'placeholder': 'I am disabled',
        })
    )
    uneditable = forms.CharField(
        max_length=100,
        help_text=u'I am uneditable and you cannot enable me with JS',
        initial=u'Uneditable',
        widget=BootstrapUneditableInput()
    )
    content = forms.ChoiceField(
        choices=(
            ("text", "Plain text"),
            ("html", "HTML"),
        ),
        help_text=u'Pick your choice',
    )
    email = forms.EmailField()
    like = forms.BooleanField(required=False)
    fruits = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ("apple", "Apple"),
            ("pear", "Pear"),
        ),
        help_text=u'As you can see, multiple checkboxes work too',
    )
    number = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'inline': True,
        }),
        choices=(
            ("3", "Three"),
            ("33", "Thirty three"),
            ("333", "Three hundred thirty three"),
        ),
        help_text=u'And can be inline',
    )
    color = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'data-demo-attr': 'bazinga'}),
        choices=(
            ("#f00", "red"),
            ("#0f0", "green"),
            ("#00f", "blue"),
        ),
        help_text=u'And we have <i>radiosets</i>',
    )
    prepended = forms.CharField(
        max_length=100,
        help_text=u'I am prepended by a P',
        widget=BootstrapTextInput(prepend='P'),
    )

    def clean(self):
        cleaned_data = super(TestForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data

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
        mensagem = forms.CharField(
        max_length=1024,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Escreva sua mensagem',
                'maxlength':"1024",
                'rows':"4",
            }
        ),
    )      
    
