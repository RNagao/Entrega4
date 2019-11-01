from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User
from api.model.Pontuacao import Pontuacao
from api.serializers import PontuacaoSerializer

class PontuacaoList(APIView):
    #/pontuacao/
    def post (self, request):
        pontos = request.data['pontos']
        funcionario_id = request.data['funcionario']

        funcionario = get_object_or_404(User, pk=funcionario_id)

        pontuacao = Pontuacao(pontos=pontos, funcionario=funcionario)
        pontuacao.save()

        data = PontuacaoSerializer(pontuacao).data
        
        return Response(data)


class PontuacaoDetail(APIView):
    def get(self, request, pk):
        #user/pontuacao/pk
        funcionario = get_object_or_404(User, pk=pk)

        pontos = Pontuacao.objects.filter(funcionario=funcionario)

        data = PontuacaoSerializer(pontos, many=True).data

        return Response(data)