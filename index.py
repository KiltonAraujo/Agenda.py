import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaUI

class IndexUI():

    def sidebar():
        op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia"])
        if op == "Manter Clientes": ManterClienteUI.main()
        if op == "Manter Serviços": ManterServicoUI.main()
        if op == "Manter Agenda": ManterAgendaUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
        
    def main():
        IndexUI.sidebar()
IndexUI.main()