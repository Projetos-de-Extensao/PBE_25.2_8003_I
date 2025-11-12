
from django.urls import path
from . import views

urlpatterns = [
    # Mapeia a URL 'monitorias/' para a função views.listar_monitorias
    path('monitorias/', views.listar_monitorias, name='lista_monitorias'),
]