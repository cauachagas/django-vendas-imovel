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


class Categoria(models.Model):
    '''
    Model que representa a Categoria do Imóvel
    '''
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = 'categoria'
        verbose_name_plural = "Categorias"
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome}"

class Imovel(models.Model):
    '''
    Model que representa o Imóvel. Essa tabela se relaciona com Categoria.
    '''
    id = models.AutoField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=255)
    endereco = models.TextField()
    criado = models.DateField(auto_now_add=True)
    imagem = models.ImageField(blank=True, null=True)
    categoria = models.ForeignKey( Categoria, on_delete=models.CASCADE, related_name='categoria')

    class Meta:
        # nome da nossa tabela
        db_table = 'imovel'
        # ordenamento por título, seguido por categoria
        ordering = ['titulo', 'categoria']

    def __str__(self):
        return f"{self.titulo}"
