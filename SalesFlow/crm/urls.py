from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, TareaViewSet, VentaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'tareas', TareaViewSet, basename='tarea')
router.register(r'ventas', VentaViewSet, basename='venta')

urlpatterns = router.urls
