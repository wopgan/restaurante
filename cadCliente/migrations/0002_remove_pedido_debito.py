# Generated by Django 4.1.5 on 2023-01-29 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadCliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='debito',
        ),
    ]