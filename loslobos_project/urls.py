from django.contrib import admin
from django.urls import path, include

from .views import IndexPage
from .views import NosotrosPage
from .views import ShopPage
from .views import ContactoPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPage.as_view(), name="index"),
    path("nosotros/", NosotrosPage.as_view(), name="nosotros"),
    path("shop/", ShopPage.as_view(), name="shop"),
    path("contacto/", ContactoPage.as_view(), name="contacto"),
    path("tienda/", include("tienda_app.urls"))
]

