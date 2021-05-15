# Imagem base
FROM python:3.8.9-slim-buster

# Criando um usuário sem super poderes
RUN useradd -ms /bin/bash django

# Usando usuário django
USER django

# Adicionando valores à variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Escolhendo o diretório de trabalho
WORKDIR /home/django/app

# Adicionando .local/bin ao PATH
ENV PATH $PATH:/home/django/.local/bin

# Copiando o arquivo requirements.txt
COPY requirements.txt .

# Instalando as depedências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante dos arquivos
COPY . .

# # Rodando o script
# RUN . ./init.sh