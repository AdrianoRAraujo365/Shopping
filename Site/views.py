from django.shortcuts import render
from .models import Departamento, Produto
# Create your views here.
def index(request):
    departamentos = Departamento.objects.all()

    context = {
        "departamentos": departamentos
    }
    return render(request, 'index.html', context)
    
def produto_lista(request):

    departamentos = Departamento.objects.all()
    produtos = Produto.objects.all()

    context = {
        "departamentos": departamentos,
        'produtos': produtos,
        'nome_categoria': "Todos Produtos"
    }
    return render(request, 'produtos.html',context)




def produto_lista_por_id(request,id):

    departamentos = Departamento.objects.all()

    context = {
        "departamentos": departamentos
    }
    return render(request, 'produtos.html',context)

def produto_detalhe(request):

    departamentos = Departamento.objects.all()

    context = {
        "departamentos": departamentos
    }
    return render(request, 'produto_detalhes.html',context)

def institucional(request):

    departamentos = Departamento.objects.all()

    context = {
        "departamentos": departamentos
    }
    return render(request, 'empresa.html',context)

def cadastro(request):

    departamentos = Departamento.objects.all()

    context = {
        "departamentos": departamentos
    }
    return render(request, 'cadastro.html',context)

def contato(request):

    departamentos = Departamento.objects.all()

    context = {
        "departamentos": departamentos
    }
    return render(request, 'contato.html',context)