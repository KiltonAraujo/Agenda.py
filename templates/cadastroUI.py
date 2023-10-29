import streamlit as st
from views import View
import pandas as pd
import time

class LoginUI():
    def main():
        st.header("Faça seu cadastro!")
        LoginUI.inserir()

    def inserir():
            nome = st.text_input("Informe o seu nome")
            email = st.text_input("Informe o seu e-mail")
            
            senha = st.text_input("Crie sua senha")
            fone = st.text_input("Informe o seu telefone")
            if st.button("Inserir"):
                if View.cliente_inserir(nome, email, senha, fone):
                    st.success("Cliente inserido com sucesso")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("E-mail já cadastrado")