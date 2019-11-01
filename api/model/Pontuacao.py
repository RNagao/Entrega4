from django.db import models
from django.contrib.auth.models import User

class Pontuacao(models.Model):
    funcionario = models.ForeignKey(User, on_delete = models.CASCADE)
    pontos = models.IntegerField(default = 0)

    def __str__(self):
        return self.pontos