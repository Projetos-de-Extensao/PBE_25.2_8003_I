from django.contrib import admin
from .models import models


@admin.action(description='Marcar conteúdos como públicos')
def make_public(modeladmin, request, queryset):
    queryset.update(is_public=True)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'creator', 'content_type', 'upload_date', 'status', 'is_public')
    list_filter = ('content_type', 'is_public', 'status', 'upload_date')
    search_fields = ('title', 'description', 'creator__username')

    ordering = ['-upload_date']

    actions = [make_public]

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'description', 'content_type')
        }),
        ('Status e Visibilidade', {
            'fields': ('status', 'is_public')
        }),
        ('Arquivos e Metadados', {
            'fields': ('file_url', 'thumbnail_url', 'creator', 'upload_date')
        }),
    )

    def has_view_permission(self, request, obj=None):
        return request.user.has_perm("content_app.view_content") or request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Criadores').exists() or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if obj and obj.creator != request.user and not request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_readonly_fields(self, request, obj=None):
        readonly = ['upload_date']
        if obj:
            readonly.append('creator')
        return readonly

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Usuario)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Monitor)
admin.site.register(Disciplina)
admin.site.register(Presenca)
admin.site.register(Mensagem)
admin.site.register(Relatorio)