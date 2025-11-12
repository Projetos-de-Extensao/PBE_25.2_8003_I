from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (
    UsuarioViewSet, ProfessorViewSet, AlunoViewSet,
    MonitorViewSet, DisciplinaViewSet, PresencaViewSet,
    MensagemViewSet, RelatorioViewSet
)

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'monitores', MonitorViewSet)
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'presencas', PresencaViewSet)
router.register(r'mensagens', MensagemViewSet)
router.register(r'relatorios', RelatorioViewSet)

# Em src/Casa/monitoria/urls.py
from django.contrib import admin
from django.urls import path, include
# Remova imports desnecessários se quiser focar no frontend integrado

urlpatterns = [
    path('admin/', admin.site.urls),
    
   
    path('', include('vagas.urls')),
    
]

