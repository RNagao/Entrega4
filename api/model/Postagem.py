from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Postagem(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    texto = models.TextField()
    dataCriada = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.texto