from rest_framework import serializers
from api.models import Postagem, Pontuacao, Usuario, Curtida, Comentario

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'

class PontuacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pontuacao
        fields = '__all__'

class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password':{'write_only': True}}