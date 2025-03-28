# Generated by Django 5.1.6 on 2025-03-07 14:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_product_is_published'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=100, verbose_name='Senha')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
            ],
        ),
        migrations.RemoveField(
            model_name='brand',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='updated_at',
        ),
        migrations.CreateModel(
            name='RegisterProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100, unique=True, verbose_name='Número de Série')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criando em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('status', models.CharField(choices=[('available', 'Disponível'), ('in_use', 'Em Uso'), ('maintenance', 'Em Manutenção'), ('retired', 'Aposentado')], default='available', max_length=20)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.brand', verbose_name='Marca')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_type', models.CharField(choices=[('entry', 'Entrada'), ('exit', 'Saída')], max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('responsible_person', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.registerproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField()),
                ('description', models.TextField()),
                ('performed_by', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.registerproduct')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'Disponível'), ('in_use', 'Em Uso'), ('maintenance', 'Em Manutenção'), ('retired', 'Aposentado')], max_length=20)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.registerproduct')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
