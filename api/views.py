from rest_framework import viewsets, generics
from api.models import Aluno, Trilha
from api.serializers import AlunoSerializer, TrilhaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class TrilhasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as trilhas"""
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer