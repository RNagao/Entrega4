from django.db import models
from api.model.Usuario import Usuario

#Entidade Pontuacao - Contém a pontuação dos funcionários cadastrados
class Pontuacao(models.Model):
    #relacionamento 1-1 com Usuario
    funcionario = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    #recebe um valor inteiro de pontos com valor padrão inicial igual a 0
    pontos = models.IntegerField(default = 0)

    def __str__(self):
        return self.pontos
