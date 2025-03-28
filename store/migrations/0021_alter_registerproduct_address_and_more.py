# Generated by Django 5.1.6 on 2025-03-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_remove_registerproduct_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerproduct',
            name='address',
            field=models.CharField(default='Endereço', max_length=255, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='registerproduct',
            name='allocator',
            field=models.CharField(default='Alocador', max_length=255, verbose_name='Alocador'),
        ),
        migrations.AlterField(
            model_name='registerproduct',
            name='leased',
            field=models.CharField(default='Locador', max_length=255, verbose_name='Locador'),
        ),
    ]
