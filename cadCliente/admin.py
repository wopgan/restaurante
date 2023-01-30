from django.contrib import admin
from .models import Cliente
from .models import Pedido

admin.site.register(Cliente)
admin.site.register(Pedido)
# Register your models here.
