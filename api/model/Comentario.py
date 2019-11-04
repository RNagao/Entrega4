from django.db import models
from api.model.Usuario import Usuario
from api.model.Postagem import Postagem

#entidade Comentario
class Comentario(models.Model):
    #relacionamento n-1 com Usuario
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    #relacionamento n-1 com Postagem
    postagem = models.ForeignKey(Postagem, on_delete = models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return self.autor + self.postagem
