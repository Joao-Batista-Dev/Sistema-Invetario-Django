# Generated by Django 5.1.6 on 2025-03-12 00:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_registeruser_cpf_alter_registeruser_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registerproduct',
            options={'ordering': ['name'], 'verbose_name': 'Registra Produto'},
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='author',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='description',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='status',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='title',
        ),
        migrations.RemoveField(
            model_name='registerproduct',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='registerproduct',
            name='date_aquisition',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='registerproduct',
            name='name',
            field=models.CharField(default='Nome Padrão', max_length=255),
        ),
        migrations.AddField(
            model_name='registerproduct',
            name='observations',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registerproduct',
            name='status_product',
            field=models.CharField(choices=[('Novo', 'Novo'), ('Bom', 'Bom'), ('Regular', 'Regular'), ('Ruim', 'Ruim')], default='Novo', max_length=20),
        ),
        migrations.AddField(
            model_name='registerproduct',
            name='supplier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='registerproduct',
            name='type',
            field=models.CharField(choices=[('Computador', 'Computador'), ('Móvel', 'Móvel'), ('Ferramenta', 'Ferramenta')], default='Computador', max_length=50),
        ),
        migrations.AlterField(
            model_name='equipmentstatus',
            name='status',
            field=models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo'), ('manutencao', 'Em Manutenção')], max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='registerproduct',
            name='serial_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
