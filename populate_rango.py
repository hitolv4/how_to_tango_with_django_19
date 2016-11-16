import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page


def populate():
    # crearemos una lista de diccionarios conteniendo las paginas
    # queremos agregar dentro de esa categoria.
    # despues vamos a crear un diccionario  para nuestra categoria
    # esto puede ser visto como algoun poco confuso, pero nos permite itinerar
    # a traves de cada estrutura de datos, y agregar datos a nuestros modelos

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 100},
        {"title": "how to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 100},
        {"title": "learn Python in 10 minutes",
         "url": "http://www.korokithakis.net/tutorial/python/",
         "views": 100}]

    django_pages = [
        {"title": "Official Django Tutorial",
            "url": "http://docs.djangoproject.com/en/1.9/intro/tutorial01/",
            "views": 100},
        {"title": "Django Rocks",
            "url": "http://www.djangorocks.com/",
            "views": 100},
        {"title": "How to tango with Django",
            "url": "http://www.tangowithdjango.com/",
            "views": 100}]

    other_pages = [
        {"title": "Bottle",
            "url": "http://bottlepy.org/docs/dev/",
            "views": 100},
        {"title": "Flask",
            "url": "http://www.flask.pocoo.org",
            "views": 100}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
            }

    # si deseas agregar mas categorias o paginas, agregala en los diccionarios
    # el codigo de abajo, va atravez del diccionario "cats" categoria.
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # para as informacion aserca de como itinerar por un diccionario
    # apropiadamente

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    # Imprime lascategorias que agegamos.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} -{1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
    # Inicia la execucion aqui!!!


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
