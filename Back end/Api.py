from fastapi import FastAPI
import funcao 

app = FastAPI(title="Gerenciador de Produtos da Loja")

@app.get("/")
def home():
    return {"Mensagem": "Bem-vindo à Loja!"}

# Listar todos produtos
@app.get("/produtos")
def catalogo():
    produtos = funcao.listar_produtos()
    lista = []
    for p in produtos:
        lista.append({
            "id": p[0],
            "nome": p[1],
            "categoria": p[2],
            "preco": float(p[3]),
            "quantidade": p[4]
        })
    return {"produtos": lista}

# Adicionar produto
@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.adicionar_produto(nome, categoria, preco, quantidade)
    return {"Mensagem": "Produto adicionado com sucesso"}

# Atualizar produto
@app.put("/produtos/{id_produto}")
def atualizar_produto(id_produto: int, novo_preco: float = None, nova_quantidade: int = None):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.atualizar_produto(id_produto, novo_preco, nova_quantidade)
        return {"Mensagem": "Produto atualizado com sucesso"}
    else:
        return {"Erro": "Produto não encontrado"}

# Deletar produto
@app.delete("/produtos/{id_produto}")
def deletar_produto(id_produto: int):
    produto = funcao.buscar_produto(id_produto)
    if produto:
        funcao.deletar_produto(id_produto)
        return {"Mensagem": "Produto deletado com sucesso"}
    else:
        return {"Erro": "Produto não encontrado"}

# Valor total em estoque
@app.get("/estoque/valor_total")
def valor_total():
    total = funcao.valor_total_estoque()
    return {"Valor_total_estoque": round(total, 2)}