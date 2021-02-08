from django.shortcuts import render
from django.views import generic

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse  
from django.urls import reverse_lazy 
from templated_email import send_templated_mail

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def post (self,request, *args, **kwargs):
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        assunto=request.POST.get('assunto')
        mmensagem=request.POST.get('mensagem')
        send_templated_mail(
        template_name='email',
        from_email= email,
        recipient_list=['cliente-site@gmail.com'],
        context={
            'nome':nome,
            'assunto':assunto,
            'email':email,
            'telefone':telefone,
            'mensagem':mmensagem
        },)
        return HttpResponseRedirect(reverse_lazy("base"))