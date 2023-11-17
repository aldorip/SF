from django.urls import path

from .views import (AddPontosView, AdicionarClienteView, AdicionarPontosView,
                    ClientesView, IndexView)

app_name = 'paginas'
urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),

    path('adicionar_cliente/', AdicionarClienteView.as_view(),
         name='adicionar_cliente'),
    path('clientes/', ClientesView.as_view(),
         name='clientes'),

    path('add__pontos/<int:cliente_id>/',
         AdicionarPontosView.as_view(), name='adicionar_pontos'),

    path('add_pontos/',
         AddPontosView.as_view(), name='add_pontos'),

]
