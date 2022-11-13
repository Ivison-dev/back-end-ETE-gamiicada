import email
from tkinter import N
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_400_BAD_REQUEST
)
from .models import Usuario
from .serializers import (
    UsuarioSerializer, 
    CadastrarUsuarioSerializer,
    LoginUsuarioSerializer
)

class LoginAPIView(APIView):
    def post(self, request, format=None):
        serializer = LoginUsuarioSerializer(data= request.data) 
        if serializer.is_valid():
            usuario = get_object_or_404(
                Usuario, 
                email = serializer.validated_data.get('email')
                )
            if usuario.senha  == serializer.validated_data.get('senha'):
                usuarioSerializer = UsuarioSerializer(usuario, many=False)
                return(Response(usuarioSerializer.data, HTTP_200_OK))
        
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors
            }, status=HTTP_400_BAD_REQUEST
        )

class CadastrarUsuarioAPIView(APIView):
    def post(self, request,format=None):
        serializer = CadastrarUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            verificacao = Usuario.objects.filter(email = serializer.validated_data.get('email'))
            if not verificacao:
                usuario = Usuario(
                    nome= serializer.validated_data.get('nome'),   # type: ignore
                    email= serializer.validated_data.get('email'), # type: ignore
                    senha= serializer.validated_data.get('senha'), # type: ignore
                    pontos_conhecimento = None
                )
                usuario.save()
                usuario_serializer = UsuarioSerializer(usuario, many=False)
                return Response(usuario_serializer.data, status=HTTP_201_CREATED)
        
        return Response(
            {
                "message": "Houveram erros de validação",
                "errors": serializer.errors
            }, status=HTTP_400_BAD_REQUEST
        )




