from rest_framework import serializers
from api.model.Postagem import Postagem
from api.model.Pontuacao import Pontuacao

from rest_framework.authtoken.models import Token

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'

class PontuacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pontuacao
        fields = '__all__'
