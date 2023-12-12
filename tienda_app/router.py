from rest_framework.routers import SimpleRouter
from .viewsets import TiendaViewSet

router = SimpleRouter()

router.register("api",TiendaViewSet)