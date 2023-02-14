from django.db import models
from django.db.models import Sum


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.TextField(help_text='Rua X, qd 55 lt X, bairro xxx Cidade/Estado')
    telefone = models.CharField(max_length=15, help_text='(62) 9999-9999')
    debito = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Débito R$')


    def update_debito(self):
        pedidos = Pedido.objects.filter(cliente=self)
        total = pedidos.exclude(pago='s').aggregate(Sum('total'))['total__sum'] or 0.00
        self.debito = total
        self.save()


    def __str__(self):
        return self.nome


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    qnt_marmita = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Quantidade de marmitas')
    valor_marmita = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor und marmita R$')
    descricao = models.TextField(default='0', verbose_name='descrição')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    pago_choices = [
        ('s', 'sim'),
        ('n', 'não'),
    ]


    pago = models.CharField(max_length=1, choices=pago_choices, default='n')


    def save(self, *args, **kwargs):
        self.total = self.qnt_marmita * self.valor_marmita
        if self.pago == 's':
            self.cliente.debito -= self.total
            self.cliente.save()
            super().save(*args, **kwargs)
            

        self.cliente.debito += self.total
        self.cliente.save()
        super().save(*args, **kwargs)
        self.cliente.update_debito()


    def delete(self, *args, **kwargs):
        self.cliente.debito -= self.total
        self.cliente.save()
        super().delete(*args, **kwargs)


    def __str__(self):
        if self.pago == 'n':
            return f'Pedido {self.id} - Cliente: {self.cliente} - {self.qnt_marmita:.0f} Marmitas - Valor a pagar R$ {self.total}'
        else:
            return f'Pedido {self.id} - Cliente: {self.cliente} - {self.qnt_marmita:.0f} Marmitas - Pedido Pago'
            
            

