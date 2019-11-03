from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    username = models.CharField(max_length=10, unique=True)
    isAdmin = models.BooleanField()
    dataCriada = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'username'
