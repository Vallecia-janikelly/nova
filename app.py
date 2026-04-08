import streamlit as st
st.set_page_config(page_title="Meu App", page_icon="", layout="wide")
st.title(" Meu Primeiro App")
st.image("lab.png", use_container_width=True)
st.markdown("## Bem-vindo!")
st.write("Este é um app simples criado com Streamlit.")
col1, col2 = st.columns(2)
with col1:
    st.info(" Aula de Informática")
with col2:
    st.success(" Aprendendo Streamlit")
st.write("")
st.link_button(" Acessar Site", "https://www.dinaldo.com.br")