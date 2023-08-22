from django.contrib import admin
from django.urls import path, include

from eventos.views import inicio, inscricao, categoria


urlpatterns = [
    path('', inicio, name='inicio'),
    path('categorias/<int:id>/', categoria, name='categoria'),
    path('inscricao/', inscricao, name='inscricao'),
    path('api/', include('rest_api.urls')),
    path('admin/', admin.site.urls),
]
