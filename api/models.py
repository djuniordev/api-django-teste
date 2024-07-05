from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
    
class Trilha(models.Model):
    TIPO = (
        ('B', 'Back-End'),
        ('F', 'Front-End'),
        ('D', 'Dados'),
    )  

    tipo = models.CharField(max_length=1, choices=TIPO, blank=False)

    def __str__(self):
        return self.tipo

