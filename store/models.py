from django.contrib.auth.models import User
from django.db import models

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
    fullname = models.CharField(max_length=200, blank=False, null=False, verbose_name='Nome Completo',)
    email = models.EmailField(unique=True,blank=False, null=False, verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Senha')
    

    class Meta:
        ordering = ['fullname']
        verbose_name = 'Usuário'

    def __str__(self):
        return self.fullname

class RegisterProduct(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponível'),
        ('in_use', 'Em Uso'),
        ('maintenance', 'Em Manutenção'),
        ('retired', 'Aposentado')
    ]

    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Número de Série",)
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Título')
    description = models.TextField(blank=False, null=False, verbose_name='Descrição')
    is_active = models.BooleanField(default=True, verbose_name='Ativo') 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Criando em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, related_name='products', verbose_name='Marca')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products', verbose_name='Categoria')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='Usuário')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    class Meta:
        ordering = ['title']
        verbose_name = 'Produto'

    def __str__(self):
        return f"{self.name} - {self.serial_number}"


class Movement(models.Model):
    MOVEMENT_TYPE = [
        ('entry', 'Entrada'),
        ('exit', 'Saída')
    ]

    product = models.ForeignKey(RegisterProduct, on_delete=models.CASCADE, verbose_name='Produto')
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPE, verbose_name='Entrada Tipo')
    quantity = models.PositiveIntegerField(verbose_name='Quantidade',)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    responsible_person = models.CharField(max_length=255, verbose_name='Colaborador')

    class Meta:
        ordering = ['product']
        verbose_name = 'Entrada e Saida'

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} ({self.quantity})"


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
    product = models.ForeignKey(RegisterProduct, on_delete=models.CASCADE, verbose_name='Produto')
    status = models.CharField(max_length=20, choices=RegisterProduct.STATUS_CHOICES, verbose_name='Status')
    changed_at = models.DateTimeField(auto_now_add=True, verbose_name='Alteração')

    class Meta:
        ordering = ['product']
        verbose_name = 'Status Equipamento'

    def __str__(self):
        return f"{self.product.name} - {self.get_status_display()} ({self.changed_at})"
