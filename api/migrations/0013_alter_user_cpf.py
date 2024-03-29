# Generated by Django 5.0.1 on 2024-01-15 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(code='cpf_invalido', message='CPF inválido', regex='^\\d{3}\\d{3}\\d{3}\\d{2}$')]),
        ),
    ]
