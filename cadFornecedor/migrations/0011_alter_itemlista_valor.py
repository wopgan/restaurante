# Generated by Django 4.1.5 on 2023-02-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadFornecedor', '0010_itemlista_remove_compra_total_compra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlista',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
