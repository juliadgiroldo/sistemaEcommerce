# Generated by Django 5.0.1 on 2024-01-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_user_password_validacao_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=180),
        ),
    ]
