import streamlit as st
from views import View
import pandas as pd
import time

class ManterServicoUI():
    def main():
        st.header("Catalogo de serviços!")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    
    def inserir():
        descricao = st.text_input("Informe a descrição do servico")
        valor = st.text_input("Informe o valor (R$)")
        duracao = st.text_input("Informe a duração (min)")

        if st.button("Inserir servico"):
            View.servico_inserir(descricao, valor, duracao)
            st.success("Serviço inserido com sucesso")
            time.sleep(1)
            st.rerun()

    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            dados = []
            for obj in servicos:
                dados.append(obj.__dict__)
            df = pd.DataFrame(dados)
            st.dataframe(df)

    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Atualização de serviços", servicos)
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            valor = st.text_input("Informe o novo valor", op.get_valor())
            duracao = st.text_input("Informe a nova duração", op.get_duracao())

        if st.button("Atualizar"):
            id = op.get_id()
            View.servico_atualizar(id, descricao, valor, duracao)
            st.success("Serviço atualizado com sucesso")
            time.sleep(3)
            st.rerun()

    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Não existem clientes para exluir")
        op = st.selectbox("exclusão de serviços :(", servicos)
        if st.button("Excluir"):
            id = op.get_id()
            View.cliente_excluir(id)
            st.success("O serviço foi de F no chat")
            time.sleep(2)
            st.rerun()