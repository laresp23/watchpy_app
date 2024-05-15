# Modelo de usuario de Django
from django.contrib.auth.models import User

# Señales de Django para realizar acciones después de guardar
from django.db.models.signals import post_save

# Decorador para conectar señales a receptores
from django.dispatch import receiver

# Importación del modelo de PerfilUsuario
from .models import PerfilUsuario

# Creación de perfil de usuario después de guardar un usuario
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)

# Guardar el perfil de usuario después de guardar un usuario si no existe
@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'perfilusuario'):
        PerfilUsuario.objects.create(user=instance)

