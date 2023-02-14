from django.utils import timezone
from django.shortcuts import redirect, render

from cadCliente.forms import ClienteForm

from .models import Pedido, Cliente

def home(request):
    hoje = timezone.now().date()
    pedidos_hoje = Pedido.objects.filter(data_date=hoje)
    context = {
        'pedidos': pedidos_hoje,
    }

    return render(request, 'home/pedidos.html')


def cadCliente(request):
    if request.method == 'post':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'home/home_cad.html', {'form': form})