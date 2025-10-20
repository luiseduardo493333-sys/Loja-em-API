# 🏬 Loja em API  

API completa para **gerenciamento de produtos de uma loja**, desenvolvida com **FastAPI** (back-end), **Streamlit** (front-end) e **PostgreSQL** como banco de dados.  
Permite **cadastrar, listar, atualizar e excluir produtos**, com controle total do estoque.  

---

## 🚀 Tecnologias Utilizadas  

| Camada | Tecnologia |
|:-------|:------------|
| **Back-end** | [FastAPI](https://fastapi.tiangolo.com/) 🐍 |
| **Banco de Dados** | PostgreSQL 🗄️ + `psycopg2` |
| **Front-end** | [Streamlit](https://streamlit.io/) 🎨 |
| **Variáveis de Ambiente** | `python-dotenv` 🔐 |
| **Servidor Local** | Uvicorn ⚡ |

---

## 🧩 Funcionalidades  

✅ Cadastrar novos produtos  
📦 Listar todos os produtos  
📝 Atualizar preço ou quantidade  
🗑️ Excluir produtos  
💰 Calcular valor total do estoque (no Streamlit)  

---

## 📁 Estrutura de Pastas  

```bash
Loja-em-API/
├── Back end/
│   ├── api.py           # Arquivo principal da API FastAPI
│   ├── funcao.py        # Funções CRUD do banco
│   ├── database.py      # Conexão com PostgreSQL
│   ├── .env             # Variáveis de ambiente
│   └── requirements.txt
└── Front end/
    ├── app.py           # Interface Streamlit
    └── requirements.txt
