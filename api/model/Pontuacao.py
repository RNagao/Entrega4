from django.db import models
from api.model.Usuario import Usuario


class Pontuacao(models.Model):
    funcionario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    pontos = models.IntegerField(default = 0)

    def __str__(self):
        return self.pontos