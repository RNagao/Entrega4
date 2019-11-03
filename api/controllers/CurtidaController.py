from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.models import Postagem, Usuario, Curtida
from api.serializers import CurtidaSerializer


class CurtidaList(APIView):
    def post (self, request):
        #/curtida/
        postagemId = request.data['postagem']
        autorId = request.data['autor']

        post = get_object_or_404(Postagem, pk=postagemId)
        autor = get_object_or_404(Usuario, pk=autorId)

        curtir = Curtida(postagem=post, autor=autor)
        curtir.save()

        data = CurtidaSerializer(curtir).data
        
        return Response(data)

class CurtidaDetail(APIView):
    def get(self, request, pk):
        #/postagem/curtida/pk
        post = get_object_or_404(Postagem, pk=pk)

        curtida = Curtida.objects.filter(postagem=post)

        data = CurtidaSerializer(curtida, many=True).data

        return Response(data)
    
    def delete(self, request,pk):
        curtida = get_object_or_404(Curtida, pk=pk)
        curtida.delete()

        data = CurtidaSerializer(curtida).data

        return Response(data)