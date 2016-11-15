from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category


def index(request):
    """Busca en la base de datos por una lista de categorias que estan guardadas
    ordena las categorias pornumero de likes en orden descendente
    coloca una lista en nuestro contxt_dic que va a ser pasado al template"""
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def rangoindex(request):
    return HttpResponse('<h1>Rango index</h1>')


def about(request):
    return HttpResponse('Rango says here is the about page.')
