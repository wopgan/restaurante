# Generated by Django 4.1.5 on 2023-02-11 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadCliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='descricao',
            field=models.TextField(default='0', verbose_name='descrição'),
        ),
    ]