from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.models import Usuario


class UsuarioList(APIView):
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data["password"]
        nome = request.data["nome"]
        is_admin = request.data["is_admin"]


        user = Usuario(nome=nome, email=email, username=username, is_admin=is_admin)
        user.set_password(password)

        validade = Usuario.objects.filter(username=user.username)
        validade_email = Usuario.objects.filter(email=user.email)

        if not (UsuarioSerializer(validade, many=True).data or UsuarioSerializer(validade_email, many=True).data):
            user.save()
            data = UsuarioSerializer(user).data
            return Response(data)

        else:
            return Response({'error': 'User already exists'})