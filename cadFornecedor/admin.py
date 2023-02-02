from django.contrib import admin
from .models import Fornecedor,Produto,Vendedor, Compra, ItemLista


admin.site.register(Fornecedor)
admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Compra)
admin.site.register(ItemLista)
# Register your models here.
