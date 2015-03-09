# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth import authenticate

class LoginView(TemplateView):
    template_name = "login.html"
    
    def post(self, request):
        loginForm = self.form_class(request.POST)
        if loginForm.isvalid():
            login = loginForm.cleaned_data['login']
            senha = loginForm.cleaned_data['password']
            user = authenticate(username=login,pasword=senha)
            if user is not None:
                if user.is_active:
                    print "Usuário autenticado e ativo!"