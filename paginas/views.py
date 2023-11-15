from django.views.generic import TemplateView


# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "paginas/modelo.html"


# Create your views here.
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
