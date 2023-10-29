import streamlit as st
from views import View
import pandas as pd
import time

class ManterClienteUI():
    def main():
        st.header("Cadastro de clientes!")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        
        senha = st.text_input("Informe a senha")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            if View.cliente_inserir(nome, email, senha, fone):
                st.success("Cliente inserido com sucesso")
                time.sleep(1)
                st.rerun()
            else:
                st.error("E-mail já cadastrado")
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dados = []
            for obj in clientes:
                id = obj.get_id()
                nome = obj.get_nome() 
                email = obj.get_email()
                fone = obj.get_fone()
                dados.append([id, nome, email, fone])

            df = pd.DataFrame(dados, columns=["id", "Nome", "E-mail", "Telefone"])
            st.dataframe(df)

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha())
            fone = st.text_input("Informe o novo fone", op.get_fone())

        if st.button("Atualizar"):
            id = op.get_id()
            if View.cliente_atualizar(id, nome, email, senha, fone):
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            else:
                st.error("E-mail já cadastrado para outro cliente")

    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Não existem clientes para exluir")
        op = st.selectbox("exclusão de Cliente :(", clientes)
        if st.button("Excluir"):
            id = op.get_id()
            View.cliente_excluir(id)
            st.success("Cliente foi de F no chat")
            time.sleep(1)
            st.rerun()
