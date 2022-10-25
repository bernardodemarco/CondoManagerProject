from models.pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: int):
        super().__init__(nome, cpf, telefone)

