# Generated by Django 5.0.1 on 2024-01-15 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_user_bairro_user_cep_user_cidade_user_complemento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cidade',
        ),
    ]