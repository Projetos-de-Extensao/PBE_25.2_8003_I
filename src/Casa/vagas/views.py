from django.shortcuts import render
from .models import Disciplina, Monitor


def listar_monitorias(request):
    disciplinas = Disciplina.objects.all()
    monitores = Monitor.objects.filter(disciplinas__in=disciplinas).prefetch_related('disciplinas')

    context = {
        'disciplinas': disciplinas,
        'monitores': monitores,
        'titulo': "Consulta de Monitorias Disponíveis"
    }

    return render(request, 'vagas/lista_monitorias.html', context)
