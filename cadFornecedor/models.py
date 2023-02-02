from django.db import models

class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ', help_text='00.000.000/0001-00')
    telefone = models.CharField(max_length=20, help_text='(62) 3333-3333')
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

class Vendedor(models.Model):
    id = models.AutoField(primary_key=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    tipo_choices = [
            ('s', 'Seco'),
            ('m', 'Molhado'),
        ]
    
    tipo = models.CharField(max_length=1, choices=tipo_choices, default='Seco')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class Produto(models.Model):
    id = models.AutoField(primary_key=True)

    tipo_choices = [
            ('s', 'Seco'),
            ('m', 'Molhado'),
    ]

    nome_produto = models.CharField(max_length=100, verbose_name='Nome Produto')
    marca_produto = models.CharField(max_length=100, verbose_name='Marca Produto')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=tipo_choices, default='Seco')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto
    
    
class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    nome_lista = models.CharField(max_length=100, verbose_name='Nome da Lista')
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor da compra', default=0)

    def __str__(self):
        return f'{self.nome_lista} esta no valor de R${self.valor_compra}'


class ItemLista(models.Model):
    id = models.AutoField(primary_key=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.valor = self.produto.preco * self.quantidade
        self.compra.valor_compra += self.valor
        self.compra.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.compra.valor_compra -= self.valor
        self.compra.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.compra.nome_lista
