# Generated by Django 5.0.1 on 2024-01-18 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_remove_carrinho_cpf_user_remove_carrinho_produtos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoitem',
            name='codigo',
        ),
    ]