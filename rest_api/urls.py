from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_api.views import categorias, api_inicio, CategoriaModelViewSet, EventoModelViewSet


app_name = 'rest_api'

router = DefaultRouter()
router.register('categorias', CategoriaModelViewSet, basename='categorias')
router.register('eventos', EventoModelViewSet, basename='eventos')


urlpatterns = [
    path('', api_inicio, name='api_inicio'),
    # path('categorias/', categorias, name='categorias'),
] + router.urls
