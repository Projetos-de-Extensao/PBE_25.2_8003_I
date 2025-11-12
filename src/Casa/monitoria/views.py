from rest_framework import viewsets
from vagas.models import Usuario, Professor, Aluno, Monitor, Disciplina, Presenca, Mensagem, Relatorio
from vagas.serializers import (
    UsuarioSerializer, ProfessorSerializer, AlunoSerializer,
    MonitorSerializer, DisciplinaSerializer, PresencaSerializer,
    MensagemSerializer, RelatorioSerializer
)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


def listar_monitorias(request):
    disciplinas = Disciplina.objects.all()
    monitores = Monitor.objects.filter(disciplinas__in=disciplinas).prefetch_related('disciplinas')

    context = {
        'disciplinas': disciplinas,
        'monitores': monitores,
        'titulo': "Consulta de Monitorias Disponíveis"
    }

    return render(request, 'vagas/lista_monitorias.html', context)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class PresencaViewSet(viewsets.ModelViewSet):
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer


class MensagemViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer


class ObtainAuthTokenRotate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username') or request.data.get('user')
        password = request.data.get('password')
        if not username or not password:
            return Response({'detail': 'Nome de usuário e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'detail': 'Credenciais inválidas.'}, status=status.HTTP_400_BAD_REQUEST)

        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response({'token': token.key})
