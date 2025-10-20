import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Loja do Luis", page_icon="🛒")
st.title("Loja do luis 🛒") 

menu = st.sidebar.radio("Navegação", ["Cátalogo", "Adicionar produto", "Atualizar produto", "Deletar produto","Valor total em estoque"])

if menu == "Cátalogo":
    st.header("Cátalogo de Produtos")
    response = requests.get(f"{API_URL}/produtos")
    produtos = response.json().get("produtos", [])
    for produto in produtos:
        st.subheader(f"{produto['nome']} (ID: {produto['id']})")
        st.write(f"Categoria: {produto['categoria']}")
        st.write(f"Preço: R$ {produto['preco']}")
        st.write(f"Quantidade em estoque: {produto['quantidade']}")
        st.markdown("---")

    else:
            st.info("Nenhum produto encontrado.")
else:
    st.error("Erro ao conectar a API")


if menu == "Adicionar produto":
        st.subheader("Adicionar produto")
        nome = st.text_input("Nome do produto:")
        categoria = st.text_input("Categoria do produto:")
        preco = st.number_input("Preço do produto")
        quantidade = st.number_input("Quantidade em estoque",step=1)
        if st.button("Adicionar produto"):
            params = {
                "nome": nome,
                "categoria": categoria,
                "preco": preco,
                "quantidade": quantidade
            }
            response = requests.post(f"{API_URL}/produtos", params=params)
            if response.status_code == 200:
                st.success("Produto adicionado com sucesso!")
            else:
                st.error("Erro ao adicionar produto")

if menu == "Atualizar produto":
        st.subheader("Atualizar produto")
        id_produto = st.number_input("ID do produto:", step=1)
        novo_preco = st.number_input("Novo preço do produto:")
        nova_quantidade = st.number_input("Nova quantidade em estoque:", step=1)
        if st.button("Atualizar produto"):
            params = {
                "novo_preco": novo_preco,
                "nova_quantidade": nova_quantidade
            }
            response = requests.put(f"{API_URL}/produtos/{id_produto}", params=params)
            if response.status_code == 200:
                st.success("Produto atualizado com sucesso!")
            else:
                st.error("Erro ao atualizar produto")