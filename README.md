Esse simples repositório tem como objetivo servir como para a criação de outros projetos. Neste projeto tentaremos criar uma pequena aplicação web de venda de imóveis onde um vendedor faz o login na aplicação, escolhe o imóvel(Apartamento ou Lote) na tela de seleção devem aparecer a localização do imóvel(endereço), valor de venda, valor de comissão do vendedor(5%), realiza a simulação de pagamento do imóvel (à vista ou 180 parcelas), escolhe o cliente que a venda será realizada e na tela final apresenta um resumo de toda a transação: Quem foi o vendedor, qual foi o imóvel, para quem foi vendido o imóvel e as condições de pagamento.

Para o desenvolvimento, está sendo utilizado Docker. Usaremos o Docker Compose para orquestrar os containers. O banco de dados escolhidos foi o PostgreSQL e usaremos o `pgadmin4` como interface gráfica do banco. Note o uso do `.dockerignore`. Este arquivo é importante para quando não queremos certos arquivos/diretórios em nossa aplicação.

## Como rodar o projeto

1. Clone o repositório;
2. docker-compose build (contruir a  imagem);
3. docker-compose up (rodar nossos serviços);
4. docker-compose down (pausar nossos serviços)

Para criar um super usuário você pode acessar o `bash` no container `docker-compose exec web bash` e depois rodar `python manage.py createsuperuser`

Depois de usar `docker-compose up`, em seguida acesse http://localhost:8000/ no seu navegador. Para acesso ao `pgadmin4` acesso  http://localhost:9000/


## Referências

- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
- https://github.com/psycopg/psycopg2/issues/684#issuecomment-538352298
- https://stackoverflow.com/a/49955098