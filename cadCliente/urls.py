from django.urls import path
from . import views

urlpatterns = [
    path('cad_cliente/', views.cadCliente, name='cad_cliente'),
]