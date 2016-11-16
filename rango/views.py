from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page


def index(request):
    """Busca en la base de datos por una lista de categorias que estan guardadas
    ordena las categorias por numero de likes en orden descendente
    coloca una lista en nuestro contxt_dic que va a ser pasado al template"""
    category_list = Category.objects.order_by('-likes')[:5]
    # busca en la base de datos por una listacon las paginas mas vistas
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}

    return render(request, 'rango/index.html', context_dict)


def rangoindex(request):
    return HttpResponse('<h1>Rango index</h1>')


def about(request):
    return HttpResponse('Rango says here is the about page.')


def show_category(request, category_name_slug):
    # crea un diccionarioque podemos pasarlo al template
    context_dict = {}

    try:
        # podemos encontrar una categoria con el nombre slug dado?
        # si no podemos, el metodo .get() levanta una exepcion DoesNotExist
        # asi que el metodo .get() retorna una instancia del modelo o exepcion
        category = Category.objects.get(slug=category_name_slug)

        # llama a todas la paginas asociadas.
        # nota el filter() retornara una lista del objeto pagina o vacia
        pages = Page.objects.filter(category=category)

        # incluye listas al template context bajo el nombre paginas.
        context_dict['pages'] = pages
        # tambien incluimos el objeto categoria des la basede datos
        # al diccionario context, usaremos esto en el template para verificar
        # que la categoria existe.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # llegamos a este punto si no encontramos la categoria espesificada.
        # no hagas nada
        # el template mostrara un mensaje "no category"
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
