from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PerfilUsuario

@receiver(post_save, sender=User)
def manejar_crear_o_actualizar_perfil(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'perfilusuario'):
        PerfilUsuario.objects.create(user=instance)
    else:
        if not hasattr(instance, 'perfilusuario'):
            PerfilUsuario.objects.create(user=instance)
        else:
            # Si el perfil de usuario ya existe, actualizamos los datos si es necesario
            perfil_usuario = instance.perfilusuario
            perfil_usuario.save()
