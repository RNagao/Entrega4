from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.models import Usuario, createToken
from api.serializers import UsuarioSerializer


class UsuarioList(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        #/usuario/
        username = request.data['username']
        email = request.data['email']
        password = request.data["password"]
        nome = request.data["nome"]
        isAdmin = request.data["isAdmin"]


        user = Usuario(nome=nome, email=email, username=username, isAdmin=isAdmin)
        user.set_password(password)

        validadeUsuario = Usuario.objects.filter(username=user.username)
        validadeNome = Usuario.objects.filter(nome=user.nome)
        validadeEmail = Usuario.objects.filter(email=user.email)

        if not (UsuarioSerializer(validadeUsuario, many=True).data or UsuarioSerializer(validadeNome, many=True).data or UsuarioSerializer(validadeEmail, many=True).data):
            user.save()
            data = UsuarioSerializer(user).data
            return Response(data)

        else:
            return Response({'error': 'User already exists'})

    def get(self, request):
        usuario = Usuario.objects.all()
        data = UsuarioSerializer(usuario, many=True).data

        return Response(data)

class UsuarioDetail(APIView):
    def delete(self, request,pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        usuario.delete()

        data = UsuarioSerializer(usuario).data

        return Response(data)