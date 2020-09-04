# XasTeste, um teste de conhecimentos técnicos

Esse é um teste de conhecimentos técnicos no qual foi apresentado um problema e precisava ser desenvolvida uma solução conforme os requisitos solicitados.

## 💻 Sobre o projeto

### A Empresa (fictícia):

A XasTree Financial Services é uma empresa que cuida de XasFinanças e XasInvestimentos de seus clientes, e, recentemente fechou parceria com uma empresa para que todos os seus funcionários pudessem realizar investimentos e terem acessoria.

### O Desenvolvedor:

Contratado pela XasTree, desenvolveu um sitema Web para substituir seu antigo sistema arcaico em versão clipper.

### O Sistema:

Tem como principal objetivo fazer com que tanto os investidores, quanto os corretorem possam verificar seus investimentos, e, para isso, foi desenvolvido um sistema utilizando as mais atuais XasTecnologias do mercado, como: 
- Python com o framework Flask;
- Banco de Dados MySQL;
- Bootstrap v4.5.2;
- Git e GitHub.

### Back-end:

Essa vertente é responsável por tratar requisições e respostas, bem como gerenciar as rotas. Os processos de CRUD (Create, Read, Update e Delete) são realizados nessa parte, sendo assim, gerencia o banco de Dados também.

### Front-end:

Responsável pela "interface gráfica" do sistema, nele se torna possível executar as funções contidas no back-end de maneira fácil e intuitiva. 

### Funcionalidades do Sistema:

- [x] Listar todos os clientes, com seus respectivos investimentos;
- [x] Pesquisar cliente informando seu email, e, após encontrado é pessível ver qual investimento está assiciado a ele;
- [x] Gerenciar clientes, nessa função é possível adicionar e remover um cliente, bem como, alterar seus dados já cadastrados, como por exemplo, o investimento vinculado a ele;
- [x] Gerenciar investimentos, nessa função é possível criar, editar ou remover um determinado investimento;
- [x] Sincronizar clientes com a API fornecida pela empresa parceira;
- [x] Reconstruir o banco de dados, apagando assim todos os clientes e investimentos associados anteriormente.

## 🚀 Como executar o projeto

### Pré-requisitos:

Ter os seguintes software instalados e executando na máquina:
- Python (versão 3.8.5) com pip;
- MySQL;
- Git.

### Instalação e configuração do ambiente:

Para que na aplicação não ocorra uma XasXception (erro), primeiramente execute os comandos do arquivo "db_create.sql" em seu banco de dados MySQL.

Após isso, abra o terminal (ou CMD) na pasta que deseja trabalhar e execute os seguintes comandos:

```bash
# Clona a aplicação do GitHub
$ git clone https://github.com/leonardopigatto/XasTeste.git

# Acessa a pasta que contém os códigos
$ cd XasTeste

# Instala as bibliotecas necessárias
$ pip install flask-mysqldb
$ pip install requests
```

### Inicialização:

Certifique-se de que os banco de dados esteja criado e executando com suas respectivas tabelas e inicialize o programa utilizando o comando: 

- OBS: lembre-se de estar na pasta que contém os arquivos baixados.

```bash
# Inicia a aplicação
$ python app.py
```

### Acesso:

Após inicializado, é possível acessar o sistema no endereço http://127.0.0.1:5000/.

## 🛠 Rotas

- `/listarClientes` -> Para listar todos os clientes;

- `/pesquisar` -> Para pesquisar um cliente;

- `/controleClientes` -> Para gerenciar os clientes;

- `/controleInvestimentos` -> Para gerenciar os investimentos;

- `/inserirAPI` -> Para importar os clientes da API;

- `/resetDB` -> Para reconstruir o banco de dados (ATENÇÃO: ISSO APAGARÁ TODOS OS DADOS PRESENTES NO BANCO);

- As demais rotas estão abtraídas na interface.

## 🚧 Possíveis melhorias

- [ ] Sistema de login com níveis de usuários;
- [ ] Utilização de Docker e Docker Composer;
- [ ] Validações de conexão com o banco de dados para não ocorrer os exceptions;
- [ ] Melhorar responsividade para smartphones por conta das tabelas;
- [ ] Incluir mais campos na tabela de investimentos, trazendo mais funções ao sistema como valor investido e dados pertinentes sobre o investimento, por exemplo, rendimento, taxa de administração, rentabilidade em um determinado período, cotização, etc.
