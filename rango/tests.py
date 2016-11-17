from django.test import TestCase
from django.core.urlresolvers import reverse
from rango.models import Category




class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        """
        ensure_views_are_positive deberia retornar Verdadero por categorias
        cuando las views son zero o positivas
        """
        cat = Category(name='test', views=1, likes=1, slug='test')
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_ensure_slug_is_ok(self):
        """
        ensure_slug_is_ok deberia retornar verdader por categorias cuando
        se esta registrando un slug
        """
        cat = Category(name='test name Hola')
        cat.save()
        self.assertEqual((cat.slug == 'test-name-hola'), True)


class IndexViewTests(TestCase):

    def test_index_views_without_categories(self):
        """
        si no existe una pregunta, muestra un mensaje apropiado
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):

        def add_cat(name, views, likes):
            c = Category.objects.get_or_create(name=name)[0]
            c.views = views
            c.likes = likes
            c.save()
            return c
        """
        revisa para estar seguro que se muestran las categorias en el index
        """
        add_cat('test', 1, 1)
        add_cat('temp', 1, 1)
        add_cat('tmp', 1, 1)
        add_cat('tmp test temp', 1, 1)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")

        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)
