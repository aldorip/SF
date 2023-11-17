from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.http import require_POST

from .models import Cliente


class IndexView(View):
    template_name = 'paginas/index.html'

    def get(self, request):
        paginas = Cliente.objects.all()
        return render(request, self.template_name, {'paginas': paginas})


class ClientesView(View):
    template_name = 'paginas/clientes.html'

    def get(self, request):
        termo_busca = request.GET.get('termo_busca', '')
        clientes_encontrados = self.buscar_clientes(termo_busca)
        return render(request, self.template_name, {'clientes_encontrados': clientes_encontrados, 'termo_busca': termo_busca})

    def post(self, request):
        termo_busca = request.POST.get('termo_busca', '')
        clientes_encontrados = self.buscar_clientes(termo_busca)
        return render(request, self.template_name, {'clientes_encontrados': clientes_encontrados, 'termo_busca': termo_busca})

    def buscar_clientes(self, termo_busca):
        if termo_busca:
            clientes = Cliente.objects.filter(
                nome__icontains=termo_busca) | Cliente.objects.filter(cpf__icontains=termo_busca)
        else:
            clientes = Cliente.objects.all()

        return clientes

    def get(self, request):
        paginas = Cliente.objects.all()
        return render(request, self.template_name, {'paginas': paginas})


class AddPontosView(View):
    template_name = 'paginas/add_pontos.html'

    def get(self, request):
        termo_busca = request.GET.get('termo_busca', '')
        clientes_encontrados = self.buscar_clientes(termo_busca)
        return render(request, self.template_name, {'clientes_encontrados': clientes_encontrados, 'termo_busca': termo_busca})

    def post(self, request):
        termo_busca = request.POST.get('termo_busca', '')
        clientes_encontrados = self.buscar_clientes(termo_busca)
        return render(request, self.template_name, {'clientes_encontrados': clientes_encontrados, 'termo_busca': termo_busca})

    def buscar_clientes(self, termo_busca):
        if termo_busca:
            clientes = Cliente.objects.filter(
                nome__icontains=termo_busca) | Cliente.objects.filter(cpf__icontains=termo_busca)
        else:
            clientes = Cliente.objects.all()

        return clientes


class AdicionarClienteView(View):
    def get(self, request):
        # Adicione lógica para lidar com solicitações GET, se necessário
        return render(request, 'paginas/adicionar_cliente.html')

    def post(self, request):
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')

        if nome and cpf:
            Cliente.objects.create(nome=nome, cpf=cpf)
            return redirect('paginas:inicio')
        else:
            # Se os dados não forem válidos, você pode lidar com isso aqui
            return HttpResponseBadRequest("Nome e CPF são obrigatórios.")


class AdicionarPontosView(View):
    def post(self, request, cliente_id):
        try:
            valor_adicionar = float(request.POST['valor_adicionar'])
        except ValueError:
            return HttpResponseBadRequest("O valor a adicionar não é um número válido.")

        cliente = Cliente.objects.get(pk=cliente_id)
        cliente.saldo += valor_adicionar
        cliente.save()

        # Calcular pontos e atualizar saldo
        pontos_adicionados = int(cliente.saldo // 20)
        cliente.pontos += pontos_adicionados
        cliente.saldo %= 20
        cliente.save()

        return redirect('paginas:clientes')
