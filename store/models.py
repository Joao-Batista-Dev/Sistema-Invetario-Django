from django.db import models
from django.utils import timezone

class RegisterUser(models.Model):
    fullname = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome Completo',)
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='Email',)
    password = models.CharField(max_length=255, verbose_name='Senha',)

    class Meta:
        ordering = ['fullname']
        verbose_name = 'Registrar Usuário'

    def __str__(self):
        return self.fullname

class RegisterProduct(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome - Produto',)
    serial_number = models.CharField(max_length=9, blank=True, null=True, verbose_name='Serial',)
    date_aquisition = models.DateTimeField(default=timezone.now, verbose_name='Data - Inicial',)
    date_end = models.DateTimeField(default=timezone.now, verbose_name='Data - Final',)
    leased = models.CharField(max_length=255, null=False, verbose_name='Locador',)
    allocator = models.CharField(max_length=255, null=False, verbose_name='Alocador',)
    address = models.CharField(max_length=255, null=False, verbose_name='Endereço',)
    observations = models.TextField(blank=True, null=True, verbose_name='Observação',)

    class Meta:
        ordering = ['name']
        verbose_name = 'Registra Produto'

    def __str__(self):
        return self.name