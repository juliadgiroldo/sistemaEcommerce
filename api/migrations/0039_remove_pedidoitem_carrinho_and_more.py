# Generated by Django 5.0.1 on 2024-01-19 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_alter_avaliacaouser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoitem',
            name='carrinho',
        ),
        migrations.RemoveField(
            model_name='pedidoitem',
            name='cpf_user',
        ),
        migrations.RemoveField(
            model_name='pedidoitem',
            name='produto',
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
        migrations.DeleteModel(
            name='PedidoItem',
        ),
    ]