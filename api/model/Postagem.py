from django.db import models
from api.model.Usuario import Usuario

class Postagem(models.Model):
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    texto = models.TextField()
    dataCriada = models.DateTimeField(auto_now=True)
    numeroComentarios = models.IntegerField(default=0)
    numeroCurtidas = models.IntegerField(default=0)

    def __str__(self):
        return self.texto