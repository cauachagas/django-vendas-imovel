from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from app.models import Cliente, Categoria, Imovel, Venda
from ninja.orm import create_schema

router = Router()

# Na entrada, o id será criado automáticamente
ClienteSchemaIn   = create_schema(Cliente, exclude=["id"])
CategoriaSchemaIn = create_schema(Categoria, exclude=["id"])
ImovelSchemaIn    = create_schema(Imovel, exclude=["id"])
VendaSchemaIn     = create_schema(Venda, exclude=["id"])

# Na saída, o id deve ser mostrado
ClienteSchemaOut   = create_schema(Cliente)
CategoriaSchemaOut = create_schema(Categoria)
ImovelSchemaOut    = create_schema(Imovel)
VendaSchemaOut     = create_schema(Venda)


@router.post("/cliente")
def registrar_cliente(request, event: ClienteSchemaIn):
    Cliente.objects.create(**event.dict())
    return event

@router.get("/cliente", response=List[ClienteSchemaOut])
def listar_clientes(request):
    return list(Cliente.objects.all())

@router.get("/cliente/{id}", response=ClienteSchemaIn)
def cliente_id(request, id: int):
    return get_object_or_404(Cliente, id=id)

@router.post("/categoria")
def registrar_categoria(request, event: CategoriaSchemaIn):
    Categoria.objects.create(**event.dict())
    return event

@router.get("/categoria", response=List[CategoriaSchemaOut])
def listar_categorias(request):
    return list(Categoria.objects.all())

@router.get("/categoria/{id}", response=CategoriaSchemaIn)
def categoria_id(request, id: int):
    return get_object_or_404(Categoria, id=id)

@router.post("/imovel")
def registrar_imovel(request, event: ImovelSchemaIn):
    Imovel.objects.create(**event.dict())
    return event

@router.get("/imovel", response=List[ImovelSchemaOut])
def listar_imoveis(request):
    return list(Imovel.objects.all())

@router.get("/imovel/{id}", response=ImovelSchemaIn)
def imovel_id(request, id: int):
    return get_object_or_404(Imovel, id=id)

@router.post("/venda")
def registrar_venda(request, event: VendaSchemaIn):
    Venda.objects.create(**event.dict())
    return event

@router.get("/venda", response=List[VendaSchemaOut])
def listar_vendas(request):
    return list(Venda.objects.all())

@router.get("/venda/{id}", response=VendaSchemaIn)
def venda_id(request, id: int):
    return get_object_or_404(Venda, id=id)