from django.db import models
from api.model.Usuario import Usuario

#Entidade Postagem - Texto com data de criação e autor que será divulgado através de notificação para outros usuários cadastrados
class Postagem(models.Model):
    #relacionamento n-1 com Usuario
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    #Possui um texto
    texto = models.TextField()
    #Possui uma data de criação
    dataCriada = models.DateTimeField(auto_now=True)
    #Contém um número variável de comentários
    numeroComentarios = models.IntegerField(default=0)
    #Contém um número variável de curtidas
    numeroCurtidas = models.IntegerField(default=0)

    def __str__(self):
        return self.texto
