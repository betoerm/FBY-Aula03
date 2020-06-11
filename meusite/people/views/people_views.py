from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.template import 
from ..models import Pessoa, Endereco

# Create your views here.
def home(request):
    return HttpResponse("Hello World")    

@require_http_methods(["GET", "POST"])
def listar(request):
    lista = Pessoa.objects.all() #gestor de banco de dados

    html = "<ul>"
    for pessoa in lista:
        html +=f"<li>{pessoa.nome} (id={pessoa.id})</li>"
    html += "</ul>"

    return HttpResponse(html)    

def detalhar(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
    return HttpResponse(f"Detalhou {pessoa.nome} (id={pessoa.id})")

def excluir(request, id_pessoa):        
    try:
        pessoa = Pessoa.objects.get(id=id_pessoa)
        if(pessoa == None):
            return HttpResponse("Pessoa não encontrada")
        else:
            pessoa.delete()
            return HttpResponse(f"Detalhou {pessoa.nome} (id={pessoa.id})")
    except ObjectDoesNotExist:
        return HttpResponse("Pessoa não encontrada")
        

def cadastrar(request):
    p = Pessoa(nome="João", idade="20")
    p.save()
    return HttpResponse(f"{p.nome} Cadastrado com sucesso")

