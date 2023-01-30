from django.contrib import admin
from .models import Fornecedor
from .models import Vendedor
from .models import Produto

admin.site.register(Fornecedor)
admin.site.register(Vendedor)
admin.site.register(Produto)    
# Register your models here.
