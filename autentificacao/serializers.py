from django.forms import ValidationError
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =  '__all__'

class CadastrarUsuarioSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=255)
    senha = serializers.CharField(max_length=100)
    
    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("O nome Precisa ter pelo menos três caracteres")
        return value

class LoginUsuarioSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    senha = serializers.CharField(max_length=100)