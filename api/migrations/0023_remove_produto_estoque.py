# Generated by Django 5.0.1 on 2024-01-15 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_user_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='estoque',
        ),
    ]