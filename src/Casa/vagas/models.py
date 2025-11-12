from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('aluno', 'Aluno'),
        ('monitor', 'Monitor'),
        ('professor', 'Professor'),
        ('admin', 'Administrador'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='aluno')

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"



class Meta:
        verbose_name_plural = 'Monitores'


class Meta:
        verbose_name_plural = 'Mensagens'


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    disciplina = models.ManyToManyField(Disciplina, related_name='professores')

    def __str__(self):
        return self.usuario.username



class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.usuario.username


class Monitor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina, related_name='monitores')
    horario_fixo = models.CharField(max_length=100, help_text="Ex: Segunda 10h-12h")

    def __str__(self):
        return self.usuario.username

class Presenca(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aluno.usuario.username} - {self.disciplina.nome} ({self.data})"



class Mensagem(models.Model):
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.remetente.username} → {self.destinatario.username}"



class Relatorio(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return f"Relatório de {self.monitor.usuario.username} - {self.disciplina.nome}"
