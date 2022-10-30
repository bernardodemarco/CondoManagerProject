from models.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: int, cargo: str, salario: int):
        super().__init__(nome, cpf, telefone)
        self.__cargo = cargo
        self.__salario = salario

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario
