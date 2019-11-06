from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.models import Postagem, Usuario
from api.serializers import PostagemSerializer


class PostagemList(APIView):
    def post (self, request):
        #/postagem/
        texto = request.data['texto']
        numeroComentarios = request.data['numComentarios']
        numeroCurtidas = request.data['numCurtidas']
        autorId = request.data['autor']

        autor = get_object_or_404(Usuario, pk=autorId)

        postagem = Postagem(texto=texto, autor=autor, numeroComentarios=numeroComentarios, numeroCurtidas=numeroCurtidas)
        postagem.save()

        data = PostagemSerializer(postagem).data
        
        return Response(data)

    def get(self, request):
        postagem = Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data

        return Response(data)


class PostagemDetail(APIView):
    def get(self, request, pk):
        #usuarios/postagem/pk
        autor = get_object_or_404(Usuario, pk=pk)

        postagem = Postagem.objects.filter(autor=autor)

        data = PostagemSerializer(postagem, many=True).data

        return Response(data)

    def delete(self, request,pk):
        postagem = get_object_or_404(Postagem, pk=pk)
        postagem.delete()

        data = PostagemSerializer(postagem).data

        return Response(data)