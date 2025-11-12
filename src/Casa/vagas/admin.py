from django.contrib import admin
from .models import *

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
    search_fields = ('nome', 'codigo')
    list_filter = ('professores',)
    ordering = ['nome']

admin.site.register(Disciplina, DisciplinaAdmin)

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'horario_fixo', 'display_disciplinas')
    search_fields = ('usuario__username', 'usuario__email')
    fieldsets = (
        ('Informações de Usuário', {'fields': ('usuario',)}),
        ('Monitoria', {'fields': ('disciplinas', 'horario_fixo')}),
    )

    def display_disciplinas(self, obj):
        return ", ".join([d.nome for d in obj.disciplinas.all()])
    display_disciplinas.short_description = 'Disciplinas'

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser and obj.usuario != request.user:
            return False
        return True

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(Monitor, MonitorAdmin)

# Em src/Casa/vagas/admin.py
# ... imports ...

# 3. Ação Personalizada para Presença (item 5)
@admin.action(description='Marcar presença confirmada nos itens selecionados')
def marcar_presenca(modeladmin, request, queryset):
    # Altera o campo 'presente' para True para os registros selecionados
    queryset.update(presente=True) 

class PresencaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'monitor', 'disciplina', 'data', 'presente')
    list_filter = ('presente', 'disciplina', 'monitor')
    # Adiciona a ação personalizada
    actions = [marcar_presenca] 

# Remova o registro simples e registre a nova classe
admin.site.register(Presenca, PresencaAdmin)