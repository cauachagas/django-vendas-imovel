from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    '''
    Model que representa o Cliente que será cadastrado
    '''
    id = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11, unique=True)
    cpf = models.CharField(max_length=11)
    data_cadastro = models.DateField(auto_now_add=True)
    imagem = models.ImageField( blank=True, null=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        # definindo nome da nossa tabela
        db_table = 'cliente'
        # ordenando por nome
        ordering = ['nome']
