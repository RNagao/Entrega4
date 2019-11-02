from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.models import Postagem, Usuario



class PostagemList(APIView):
    #/postagem/
    def post (self, request):
        texto = request.data['texto']
        autor_id = request.data['autor']

        autor = get_object_or_404(User, pk=autor_id)

        postagem = Postagem(texto=texto, autor=autor)
        postagem.save()

        data = PostagemSerializer(postagem).data
        
        return Response(data)


class PostagemDetail(APIView):
    def get(self, request, pk):
        #user/postagem/pk
        autor = get_object_or_404(User, pk=pk)

        postagem = Postagem.objects.filter(autor=autor)

        data = PostagemSerializer(postagem, many=True).data

        return Response(data)