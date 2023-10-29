import json

class Cliente:
  def __init__(self, id, nome, email, senha, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
    self.__senha = senha

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_senha(self): return self.__senha
  def get_fone(self): return self.__fone

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_senha(self, senha): self.__senha = senha
  def set_fone(self, fone): self.__fone = fone

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and x.__senha == self.__senha and self.__fone == x.__fone:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha} - {self.__fone}"


class NCliente:
  __clientes = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    for cliente in cls.__clientes:
      if cliente.get_email() == obj.get_email():
        return False
    id = 0
    for aux in cls.__clientes:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)
    cls.salvar()
    return True

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__clientes

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__clientes:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def veri_email(cls, email):
    cls.abrir()
    for obj in cls.__clientes:
      if obj.get_email() == email: return ValueError()

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    for cliente in cls.__clientes:
      if cliente.get_email() == obj.get_email() and cliente.get_id() != obj.get_id():
        return False
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_nome(obj.get_nome())
      aux.set_email(obj.get_email())
      aux.set_senha(obj.get_email())
      aux.set_fone(obj.get_fone())
      cls.salvar()
    return True

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__clientes.remove(aux)
      cls.salvar()


  @classmethod
  def abrir(cls):
    cls.__clientes = []
    try:
      with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          aux = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__senha"], obj["_Cliente__fone"])
          cls.__clientes.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.__clientes, arquivo, default=vars)