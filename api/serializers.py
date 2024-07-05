from rest_framework import serializers
from api.models import Aluno, Trilha

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class TrilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trilha
        fields = '__all__'