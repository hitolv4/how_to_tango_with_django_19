from django.template.defaultfilters import slugify
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwag):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwag)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    verbose_name = 'Pagina'
    verbose_name_plural = 'Paginas'
