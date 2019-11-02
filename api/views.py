from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.controllers.PostagemController import PostagemList, PostagemDetail
from api.controllers.PontuacaoController import PontuacaoList, PontuacaoDetail

from api.serializers import PostagemSerializer, PontuacaoSerializer, UsuarioSerializer

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from django.contrib.auth import authenticate


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
    
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status = status.HTTP_400_BAD_REQUEST)

