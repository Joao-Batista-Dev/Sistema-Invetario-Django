# Generated by Django 5.1.6 on 2025-03-21 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_delete_brand_delete_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade'),
        ),
    ]
