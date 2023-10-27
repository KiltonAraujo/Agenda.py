import json
class Cliente:
  def __init__(self,id,nome,email,fone):
    self.__idC = id
    self.__nome = str()
    self.__email = str()
    self.__fone = str()

  def set_nome(self, nome):
    if nome != "": self.__nome = nome
    else: raise ValueError()
      
  def set_email(self, email):
    if email != "": self.__email = email
    else: raise ValueError()
      
  def set_fone(self, fone):
    if fone != "": self.__fone = fone
    else: raise ValueError()
  
  def get_idC(self):return self.__idC
  
  def get_nome(self):return self.__nome
  
  def get_email(self):return self.__email
  
  def get_fone(self):return self.__fone
  
  def __str__(self):
    return f"cliente id: {self.__id} - nome: {self.__nome} - {self.__email} - {self.__fone}"



class NCliente:
  __clientes = []
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"],cliente["_Cliente__email"], cliente["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls, arquivo, default = vars)

  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)
    NCliente.salvar()

  @classmethod
  def listar(cls):
    NCliente.abrir()    
    return cls.__clientes 

  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None

  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()


  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)    
    NCliente.salvar()