
def upload_imagem_cliente(instance, filename):
    return f"{instance.nome}-{instance.email}"

def upload_imagem_imovel(instance, filename):
    return f"{instance.titulo}-{instance.criado}"
