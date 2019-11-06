from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager

#Entidade Usuario - Guarda as informações dos usuários cadastrados na plataforma
class Usuario(AbstractBaseUser):
    #Possui um nome com máximo de 30 caracteres
    nome = models.CharField(max_length=30, unique=True)
    #Possui um e-mail atrelado
    email = models.EmailField()
    #Possui um nome de usuário (como ele prefere ser referenciado na plataforma)
    username = models.CharField(max_length=10, unique=True)
    #Pode ou não ser um usuário tipo administrador
    isAdmin = models.BooleanField()
    #Guarda a data em que foi criado na plataforma
    dataCriada = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'username'
