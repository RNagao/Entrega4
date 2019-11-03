from django.db import models
from api.model.Usuario import Usuario
from api.model.Postagem import Postagem


class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete = models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return self.autor + self.postagem
