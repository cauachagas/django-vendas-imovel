from django.db import models
from django.contrib.auth.models import User
from cpf_field.models import CPFField
from helpers.upload_name import upload_imagem_cliente, upload_imagem_imovel
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Cliente(models.Model):
    '''
    Model que representa o Cliente que será cadastrado
    '''
    id = models.AutoField(primary_key=True, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11, unique=True)
    cpf = CPFField(unique=True)
    data_cadastro = models.DateField(auto_now_add=True)
    imagem = models.ImageField(
        upload_to=upload_imagem_cliente, blank=True, null=True
    )
    
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
    imagem = models.ImageField(
        upload_to=upload_imagem_imovel, blank=True, null=True
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria')

    class Meta:
        # nome da nossa tabela
        db_table = 'imovel'
        # ordenamento por título, seguido por categoria
        ordering = ['titulo', 'categoria']

    def __str__(self):
        return f"{self.titulo}"

class Venda(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imovel = ChainedForeignKey(
        "Imovel",
        chained_field="categoria",
        chained_model_field="categoria",
        show_all=False,
        auto_choose=True,
    )

    @property
    def endereco(self):
        '''
        Retorna o endereço do imóvel.
        '''
        return "%s"%(self.imovel.endereco)
        
    valor = models.IntegerField(
        default=100000,
        help_text = "O corretor tem direito à 5% de comissão"
    )
    
    corretor = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    ESCOLHA_PAGAMENTOS = (
        ("À vista", "À vista"),
        ("Parcelado", "180 parcelas"),
    )
    pagamento = models.CharField(max_length=9, choices=ESCOLHA_PAGAMENTOS, blank=False, null=False)
    
    @property
    def comissao(self):
            return self.valor * (5.0/100)

    class Meta:
        db_table = 'venda'
        # Ordenando pelo id mais recente
        ordering = ['-id']

    def __str__(self):
        # Adicionando um outro identificador para facilitar a leitura
        return f"{self.id}-{self.imovel}"