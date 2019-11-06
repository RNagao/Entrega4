from django.db import models
from api.model.Comentario import Comentario
from api.model.Curtida import Curtida
from api.model.Pontuacao import Pontuacao
from api.model.Postagem import Postagem
from api.model.Usuario import Usuario

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createToken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    