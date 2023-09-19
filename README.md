# Olá, esse é o repositório do projeto Assistente Vitual 🤖

Para mais informações sobre o projeto, consuma esse README e, caso ainda surja alguma dúvida, entre em contato comigo! 

Neste projeto eu implementei o que aprendi até então no bootcamp de Ciência de Dados da DIO, criando um ETL simples utilizando a API da openai.

Esse projeto é composto por dois módulos:

- **Módulo de criação do banco de dados**, em que o arquivo no formato json com informações dos clientes é gerado;

- **Módulo de ETL** onde de fato são realizadas as etapas de extração, transformação e carregamento.

Meu objetivo com esse projeto é a atualização de um banco de dados com informação de clientes de uma loja de brinquedos. A partir da idade deles, sugestões de compras na loja são adicionadas ao perfil dos clientes.

🚨 *Nesse projeto foi utilizada a API da openai, uma ferramenta disponível gratuitamente de forma limitada*

<details>
  <summary><strong> ➡️ Informações Importantes </strong></summary><br /> 
  Para esse projeto é indicado o uso de um ambiente virtual. Para isso basta seguir os seguintes passos:

  1️⃣ **criar o ambiente virtual**

  ```python
  python3 -m venv .venv
  ```

  2️⃣ **ativar esse ambiente**

  ```bash
  source .venv/bin/activate
  ```

  3️⃣ **instalar as dependências no ambiente virtual**

  ```python
  python3 -m pip install -r dev-requirements.txt
  ```

  ➕ Caso precise desativar o ambiente virtual, use o comando
  ```python
  deactivate
  ```
  
  Mas lembre-se de ativar o ambiente virtual novamente quando voltar a trabalhar no projeto! 

</details>

<details>
  <summary><strong> ➡️ Passo a Passo </strong></summary><br /> 
  Primeiro, devemos criar nosso banco de dados para o projeto. 

  O arquivo `clients` fica responsável por essa tarefa, e através do uso da biblioteca `faker`, criamos informações como nome, idade e código do cliente. 

  1️⃣ **gerar banco de dados**

  ```python
  python3 data_creation/client.py
  ```

  Ao rodar esse comando, será perguntado a quantidade de clientes desejada.
  
  🚨 *A versão gratuita da API que estamos utilizando permite apenas 3 consultas por minuto, o que significa uma quantidade limitada a 3 clientes.*
  
  Nosso banco de dados é um arquivo .json, e podemos acessá-lo dentro da pasta `data` sob o nome `clients_data`.

  Para adicionar as sugestões de compra na loja, iremos utilizar a API da openai. 
  Para ser utilizada, é necessária a inserção de uma chave chamada API key no arquivo `client_products`. Essa chave pode ser encontrada no seu perfil cadastrado no site [da OpenAI](https://openai.com/) dentro da opção `View API keys` no menu da sua conta. 

  2️⃣ **atualizar banco de dados**

  ```python
  python3 data_update/client_products.py
  ```

  Esse arquivo é o responsável por fazer a conexão com a API de inteligência artificial e gera a lista de produtos indicados para a faixa etária do cliente, que você pode conferir acessando novamente o arquivo `clients_data`.

