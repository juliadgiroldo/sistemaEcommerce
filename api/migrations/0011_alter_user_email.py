# Generated by Django 5.0.1 on 2024-01-15 17:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=256, unique=True, validators=[django.core.validators.RegexValidator(code='email_invalido', message='Email invalido', regex='^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}$')]),
        ),
    ]