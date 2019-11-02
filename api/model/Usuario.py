from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    username = models.CharField(max_length=10, unique=True)
    isAdmin = models.BooleanField()
    dataCriada = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username'