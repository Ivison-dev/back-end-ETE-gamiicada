from django.urls import path
from .views import LoginAPIView, CadastrarUsuarioAPIView

urlpatterns = [
    path('login', LoginAPIView.as_view()),
    path('cadastro', CadastrarUsuarioAPIView.as_view()),
]
