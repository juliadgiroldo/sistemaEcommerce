# Generated by Django 5.0.1 on 2024-01-16 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_produto_fornecedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='fornecedor',
        ),
    ]
