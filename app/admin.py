from django.contrib import admin
import easy

# Register your models here.
from app.models import Cliente, Categoria, Imovel, Venda

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "data_cadastro")
    search_fields = ('nome',)
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ('nome',)

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ("id", "imagem", "categoria", "titulo", "endereco")
    search_fields = ('titulo', "endereco")

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    fields = ("categoria", "imovel", "valor", "cliente", 'corretor', 'pagamento')
    list_display = ('id', 'link_categoria','link_imovel', 'endereco', 'valor', 'pagamento', 'link_cliente', 'comissao')
    search_fields = ("categoria", "imovel", "cliente", 'corretor', 'pagamento')


    link_imovel = easy.ForeignKeyAdminField('imovel')
    link_cliente = easy.ForeignKeyAdminField('cliente')
    link_categoria = easy.ForeignKeyAdminField('categoria')