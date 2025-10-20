from conexao import conectar
def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50),
                    preco NUMERIC(10,2),
                    quantidade INT
                )
            """)
            conexao.commit()
        finally:
            cursor.close()
            conexao.close()

def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        finally:
            cursor.close()
            conexao.close()

adicionar_produto("Teclado Gamer", "Periféricos", 250.00, 15)

def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos ORDER BY id")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(id_produto, preco=None, quantidade=None):
    conexao, cursor = conectar()
    if conexao:
        try:
            if preco is not None:
                cursor.execute("UPDATE produtos SET preco = %s WHERE id = %s", (preco, id_produto))
            if quantidade is not None:
                cursor.execute("UPDATE produtos SET quantidade = %s WHERE id = %s", (quantidade, id_produto))
            conexao.commit()
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
            conexao.commit()
        finally:
            cursor.close()
            conexao.close()