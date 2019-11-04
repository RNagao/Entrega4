from django.db import models
from api.model.Usuario import Usuario

#Entidade Postagem - Texto com data de criação e autor que será divulgado através de notificação para outros usuários cadastrados
class Postagem(models.Model):
    #relacionamento n-1 com Usuario
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    texto = models.TextField()
    dataCriada = models.DateTimeField(auto_now=True)
    numeroComentarios = models.IntegerField(default=0)
    numeroCurtidas = models.IntegerField(default=0)

    def __str__(self):
        return self.texto
