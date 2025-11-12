from django.contrib import admin
from .models import Usuario, Professor, Aluno, Monitor, Disciplina, Presenca, Mensagem, Relatorio
from django.utils.html import format_html

@admin.action(description='Marcar presença confirmada nos itens selecionados')
def marcar_presenca(modeladmin, request, queryset):
    queryset.update(presente=True)
marcar_presenca.allowed_permissions = ('change',)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'tipo', 'is_staff', 'is_active')
    list_filter = ('tipo', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'tipo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')

class AlunoAdmin(admin.ModelAdmin):
    def nome_completo(self, obj):
        return f"{obj.usuario.first_name} {obj.usuario.last_name}"
    nome_completo.short_description = 'Nome do Aluno'

    list_display = ('nome_completo', 'matricula', 'usuario')
    search_fields = ('matricula', 'usuario__username', 'usuario__email')
    list_filter = ('matricula',)

class ProfessorAdmin(admin.ModelAdmin):
    def nome_completo(self, obj):
        return f"{obj.usuario.first_name} {obj.usuario.last_name}"
    nome_completo.short_description = 'Nome do Professor'

    def display_disciplinas(self, obj):
        return ", ".join([d.nome for d in obj.disciplina.all()])
    display_disciplinas.short_description = 'Disciplinas'

    list_display = ('nome_completo', 'usuario', 'display_disciplinas')
    search_fields = ('usuario__username', 'usuario__email')
    list_filter = ('disciplina',)
    fieldsets = (
        (None, {'fields': ('usuario', 'disciplina')}),
    )

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
    search_fields = ('nome', 'codigo')
    list_filter = ('monitores', 'professores')
    ordering = ['nome']

class MonitorAdmin(admin.ModelAdmin):
    def display_disciplinas(self, obj):
        return ", ".join([d.nome for d in obj.disciplinas.all()])
    display_disciplinas.short_description = 'Disciplinas de Monitoria'

    list_display = ('usuario', 'horario_fixo', 'display_disciplinas')
    search_fields = ('usuario__username', 'usuario__email')
    list_filter = ('disciplinas',)
    ordering = ['usuario__username']
    fieldsets = (
        (None, {'fields': ('usuario', 'horario_fixo')}),
        ('Disciplinas Associadas', {'fields': ('disciplinas',)}),
    )

class PresencaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'monitor', 'disciplina', 'data', 'presente')
    list_filter = ('presente', 'disciplina', 'monitor', 'data')
    search_fields = ('aluno__usuario__username', 'monitor__usuario__username')
    ordering = ['-data']
    actions = [marcar_presenca]

class MensagemAdmin(admin.ModelAdmin):
    def conteudo_curto(self, obj):
        return obj.conteudo[:50] + '...' if len(obj.conteudo) > 50 else obj.conteudo
    conteudo_curto.short_description = 'Conteúdo'

    list_display = ('remetente', 'destinatario', 'data_envio', 'conteudo_curto')
    list_filter = ('data_envio',)
    search_fields = ('remetente__username', 'destinatario__username', 'conteudo')
    readonly_fields = ('data_envio', 'remetente', 'destinatario')

class RelatorioAdmin(admin.ModelAdmin):
    def conteudo_curto(self, obj):
        return obj.conteudo[:50] + '...' if len(obj.conteudo) > 50 else obj.conteudo
    conteudo_curto.short_description = 'Conteúdo do Relatório'

    list_display = ('monitor', 'disciplina', 'data', 'conteudo_curto')
    list_filter = ('disciplina', 'monitor', 'data')
    search_fields = ('monitor__usuario__username', 'disciplina__nome', 'conteudo')
    ordering = ['-data']
    readonly_fields = ('data', 'monitor', 'disciplina')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Presenca, PresencaAdmin)
admin.site.register(Mensagem, MensagemAdmin)
admin.site.register(Relatorio, RelatorioAdmin)