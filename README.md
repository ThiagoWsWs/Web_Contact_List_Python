# Web_Contact_List_Python
Agenda de Contatos Web é uma aplicação desenvolvida com Flask e MySQL para gerenciamento de contatos. O sistema permite cadastrar, listar, buscar, editar e excluir contatos através de uma interface web responsiva construída com Bootstrap. Também possui validação de e-mail e mensagens de feedback para melhorar a experiência do usuário.

# 📒 Agenda de Contatos Web

Uma aplicação web desenvolvida com Flask e MySQL para gerenciamento de contatos. O sistema permite cadastrar, pesquisar, editar e excluir contatos através de uma interface simples e responsiva construída com Bootstrap.

## ✨ Funcionalidades

* Cadastro de contatos
* Busca por nome
* Edição de informações
* Exclusão de registros
* Validação de e-mail
* Feedback visual para operações realizadas
* Interface responsiva

## 🛠️ Tecnologias Utilizadas

* Python
* Flask
* MySQL
* Bootstrap 5
* python-dotenv
* mysql-connector-python

## 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/agenda-contatos.git
cd agenda-contatos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=agenda_contatos
```

Crie o banco de dados:

```sql
CREATE DATABASE agenda_contatos;

USE agenda_contatos;

CREATE TABLE contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(150) NOT NULL
);
```

Execute a aplicação:

```bash
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

## 📂 Estrutura do Projeto

```text
agenda-contatos/
├── app.py
├── contato.py
├── database.py
├── requirements.txt
├── templates/
│   └── index.html
└── .env
```

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar conceitos de desenvolvimento web com Flask, integração com banco de dados MySQL e implementação de operações CRUD em aplicações web.

---

Desenvolvido por Thiago Winicius da Silva.
