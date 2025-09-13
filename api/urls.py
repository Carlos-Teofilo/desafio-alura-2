from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import ReceitaViewSet, DespesaViewSet

router = DefaultRouter()
router.register('receitas', ReceitaViewSet, basename='receitas')
router.register('despesas', DespesaViewSet, basename='despesas')

urlpatterns = router.urls