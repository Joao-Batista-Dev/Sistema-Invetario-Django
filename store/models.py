from django.contrib.auth.models import User
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Criando em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    # ordenacao dos registro
    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = name = models.CharField(max_length=200, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Criando em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    # ordenacao dos registro
    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    serial = models.CharField(max_length=9, unique=True, verbose_name="Número de Série", default="")
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Criando em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='Categoria')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='Usuário')

    # ordenacao dos registro
    class Meta:
        ordering = ['title']
        verbose_name = 'Produto'

    def __str__(self):
        return self.title