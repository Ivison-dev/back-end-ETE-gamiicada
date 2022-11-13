from statistics import mode
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False, primary_key=True)
    senha = models.CharField(max_length=100, null=False, blank=False)
    pontos_conhecimento = models.PositiveIntegerField(null=True)



