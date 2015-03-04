# -*- coding : utf-8 -*-
import os
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from requisitador.models import Requisicao, Sistema

def addSistema():
    pass
def addRequisicao():
    pass
def populate():
    users =(
        User.objects.create_user('makeli', 'makeli.juca@ruimail.md', 'makeli'),
        User.objects.create_user('rodrigo', 'rodrigo@ruimail.md', 'rodrigo'),
        User.objects.create_user('sabia', 'sabia@ruimail.md', 'sabia'),
        User.objects.create_user('caio', 'caio.prado@ruimail.md', 'caio'),
        User.objects.create_user('marcelo', 'marcelo@ruimail.md', 'marcelo'),
        User.objects.create_user('mauricio', 'mauricio@ruimail.md', 'mauricio'),
        User.objects.create_user('elisafa', 'elisafa@ruimail.md', 'elisafa'),
        User.objects.create_user('valber', 'valber@ruimail.md', 'valber'),
        User.objects.create_user('neila', 'neila@ruimail.md', 'neila'),
        User.objects.create_user('geila', 'marcelo@ruimail.md', 'geila'),
    )
    ctReq = ContentType.objects.get_for_model(Requisicao)
    ctSys = ContentType.objects.get_for_model(Sistema)
    
    criar_requisicao = Permission.objects.get_by_natural_key('add_requisicao', 'requisitador', Requisicao)
    alterar_requisicao = Permission.objects.get_by_natural_key('change_requisicao', 'requisicao', Requisicao)
    remover_requisicao = Permission.objects.get_by_natural_key('delete_requisicao', 'requisitador', Requisicao)
    
    criar_sistema = Permission.objects.get_by_natural_key('add_sistema', 'requisitador', Sistema)
    alterar_sistema = Permission.objects.get_by_natural_key('change_sistema', 'requisitador', Sistema)
    remover_sistema = Permission.objects.get_by_natural_key('delete_sistema', 'requisitador', Sistema)
    
    
    for u in users:
        t = User.objects.create_user('asasd','asdas@asd.d','asdef')
        t.
    

if __name__ == '__main__':
    print 'Inicio do código para popular o banco'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SysFuncao.settings')
    