from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.models import Postagem, Usuario, Comentario
from api.serializers import ComentarioSerializer


class ComentarioList(APIView):
    def post (self, request):
        #/comentario/
        texto_comentario = request.data['texto']
        postagemId = request.data['postagem']
        autorId = request.data['autor']

        post = get_object_or_404(Postagem, pk=postagemId)
        autor = get_object_or_404(Usuario, pk=autorId)

        comentar = Comentario(texto=texto_comentario, postagem=post, autor=autor)
        comentar.save()

        data = ComentarioSerializer(comentar).data
        
        return Response(data)

class ComentarioDetail(APIView):
    def get(self, request, pk):
        #/postagem/comentario/pk
        post = get_object_or_404(Postagem, pk=pk)

        comentario = Comentario.objects.filter(postagem=post)

        data = ComentarioSerializer(comentario, many=True).data

        return Response(data)

    def delete(self, request,pk):
        comentario = get_object_or_404(Comentario, pk=pk)
        comentario.delete()

        data = ComentarioSerializer(comentario).data

        return Response(data)