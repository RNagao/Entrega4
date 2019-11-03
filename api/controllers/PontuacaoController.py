from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.models import Pontuacao, Usuario
from api.serializers import PontuacaoSerializer

class PontuacaoList(APIView):
    def post (self, request):
        #/pontuacao/
        pontos = request.data['pontos']
        funcionarioId = request.data['funcionario']

        funcionario = get_object_or_404(Usuario, pk=funcionarioId)

        pontuacao = Pontuacao(pontos=pontos, funcionario=funcionario)
        pontuacao.save()

        data = PontuacaoSerializer(pontuacao).data
        
        return Response(data)

    def get(self, request):
        pontuacao = Pontuacao.objects.all()
        data = PontuacaoSerializer(pontuacao, many=True).data

        return Response(data)


class PontuacaoDetail(APIView):
    def get(self, request, pk):
        #usuarios/pontuacao/pk
        funcionario = get_object_or_404(Usuario, pk=pk)

        pontos = Pontuacao.objects.filter(funcionario=funcionario)

        data = PontuacaoSerializer(pontos, many=True).data

        return Response(data)

    def delete(self, request,pk):
        pontuacao = get_object_or_404(Pontuacao, pk=pk)
        pontuacao.delete()

        data = PontuacaoSerializer(pontuacao).data

        return Response(data)