from django.contrib import admin

# Register your models here.
from app.models import Cliente, Categoria, Imovel, Venda

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "data_cadastro")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ("id", "imagem", "categoria", "titulo", "endereco")

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    fields = ("categoria", "imovel", "valor", "cliente", 'corretor', 'pagamento')
    list_display = ('id', 'categoria','imovel', 'endereco', 'valor', 'pagamento', 'comissao')
