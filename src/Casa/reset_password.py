import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoria.settings')
django.setup()

from vagas.models import Usuario

user = Usuario.objects.get(username='admin')
user.set_password('1234567')
user.save()

print("✅ Senha do admin resetada com sucesso!")
print("Username: admin")
print("Senha: 1234567")
