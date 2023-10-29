from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda
import datetime

class View():
    def cliente_inserir(nome, email, senha, fone):
        cliente = Cliente(0, nome, email, senha, fone)
        return NCliente.inserir(cliente)

    def cliente_listar():
        return NCliente.listar()
    def cliente_listar_id(id):
        return NCliente.listar_id(id)

    def cliente_atualizar(id, nome, email,senha,fone):
        Cliente = Cliente(id,nome,email,senha,fone)
        return NCliente.atualizar(Cliente)

    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        return NCliente.excluir(cliente)
    
    def servico_inserir(descricao, valor, duracao):
        servico = Servico(0, descricao, valor, duracao)
        return NServico.inserir(servico)

    def servico_listar():
        return NServico.listar()
    def servico_listar_id(id):
        return NServico.listar_id(id)
    
    def servico_atualizar(id, descricao, valor, duracao):
        servico = Servico(id, descricao, valor, duracao)
        return NServico.atualizar(servico)
    
    def servico_excluir(id):
        servico = Servico(id, "", "", "")
        return NServico.excluir(servico)
    
    def agenda_inserir(data, confirmado, id_cliente, id_servico):
        agenda = Agenda(0, data, confirmado, id_cliente, id_servico)
        return NAgenda.inserir(agenda)

    def agenda_listar():
        return NAgenda.listar()
    
    def agenda_atualizar(id, data, confirmado, nome_cliente, descricao_servico):
        agenda = Agenda(id, data, confirmado, nome_cliente, descricao_servico)
        NAgenda.atualizar(agenda)

    def agenda_excluir(id):
        agenda = Agenda(id, "", "", "", "")
        NAgenda.excluir(agenda)

    def agenda_abrir_agenda(data, hinicio, hfim, intervalo):
        data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
        data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
        delta = datetime.timedelta(minutes = intervalo) 
        aux = data_inicio
        while aux <= data_fim :
            NAgenda.inserir(Agenda(0, aux, False, 0, 0))
            aux = aux + delta