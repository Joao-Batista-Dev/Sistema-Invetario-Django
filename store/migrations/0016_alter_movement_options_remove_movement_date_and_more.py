# Generated by Django 5.1.6 on 2025-03-12 14:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_registerproduct_serial_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movement',
            options={},
        ),
        migrations.RemoveField(
            model_name='movement',
            name='date',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='product',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='responsible_person',
        ),
        migrations.AddField(
            model_name='movement',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='movement',
            name='expected_return',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movement',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movement',
            name='register_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.registerproduct'),
        ),
        migrations.AddField(
            model_name='movement',
            name='responsible',
            field=models.CharField(default='Não especificado', max_length=100),
        ),
        migrations.AddField(
            model_name='movement',
            name='sector',
            field=models.CharField(default='Não especificado', max_length=100),
        ),
        migrations.AddField(
            model_name='movement',
            name='status',
            field=models.CharField(default='Pendente', max_length=50),
        ),
        migrations.AlterField(
            model_name='movement',
            name='movement_type',
            field=models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída')], max_length=10),
        ),
    ]
