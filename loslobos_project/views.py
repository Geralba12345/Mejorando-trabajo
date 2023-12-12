from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"

class NosotrosPage(TemplateView):
    template_name = "nosotros.html"

class ShopPage(TemplateView):
    template_name = "shop.html"

class ContactoPage(TemplateView):
    template_name = "contacto.html"