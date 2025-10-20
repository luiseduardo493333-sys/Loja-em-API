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