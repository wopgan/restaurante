from django.shortcuts import render, redirect
from cadCliente.models import Pedido
from cadCliente.models import Cliente


def home(request):
    pedidos = Pedido.objects.all()
    context = {
        'pedidos': pedidos,
    }
    return render(request, 'home/home.html', context)

def cadCliente(request):
    if request.method == 'post':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        cliente = Cliente(nome=nome, endereco=endereco, telefone=telefone, email=email)
        cliente.save()

        return redirect('home')

    return render(request, 'home/home_cad.html')

