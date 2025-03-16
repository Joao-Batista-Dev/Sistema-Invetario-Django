from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')

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

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name

class RegisterUser(models.Model):
    fullname = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome Completo')
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Senha')

    class Meta:
        ordering = ['fullname']
        verbose_name = 'Usuário'

    def __str__(self):
        return self.fullname

class RegisterProduct(models.Model):
    name = models.CharField(max_length=255, default="Nome Padrão")
    type = models.CharField(max_length=50, choices=[
        ('Computador', 'Computador'),
        ('Móvel', 'Móvel'),
        ('Ferramenta', 'Ferramenta'),
    ], default='Computador')  # Valor padrão adicionado

    serial_number = models.CharField(max_length=9,)
    date_aquisition = models.DateTimeField(default=timezone.now)
    status_product = models.CharField(max_length=20, choices=[
        ('Novo', 'Novo'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    ], default='Novo')
    
    supplier = models.CharField(max_length=255, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Registra Produto'

    def __str__(self):
        return self.name

class Movement(models.Model):
    MOVEMENT_TYPE_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]
    
    register_product = models.ForeignKey(RegisterProduct, on_delete=models.CASCADE, null=True, blank=True)
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPE_CHOICES)
    date_time = models.DateTimeField(default=timezone.now)
    responsible = models.CharField(max_length=100, default="Não especificado")
    sector = models.CharField(max_length=100, default="Não especificado")
    status = models.CharField(max_length=50, default="Pendente")
    reason = models.TextField(blank=True, null=True)
    expected_return = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.movement_type} - {self.register_product.name} - {self.date_time}"
    
class Maintenance(models.Model):
    product = models.ForeignKey(RegisterProduct, on_delete=models.CASCADE, verbose_name='Produto')
    maintenance_date = models.DateField(verbose_name='Data da Manuteção')
    description = models.TextField(verbose_name='Descrição')
    performed_by = models.CharField(max_length=255, verbose_name='Responśavel pela Manuteção')

    class Meta:
        ordering = ['product']
        verbose_name = 'Manutenção'

    def __str__(self):
        return f"Manutenção - {self.product.name} ({self.maintenance_date})"
    
class EquipmentStatus(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('manutencao', 'Em Manutenção'),
    ]

    product = models.ForeignKey(RegisterProduct, on_delete=models.CASCADE, verbose_name='Produto')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Status')
    changed_at = models.DateTimeField(auto_now_add=True, verbose_name='Alteração')

    class Meta:
        ordering = ['product']
        verbose_name = 'Status Equipamento'

    def __str__(self):
        return f"{self.product.name} - {self.get_status_display()} ({self.changed_at})"
