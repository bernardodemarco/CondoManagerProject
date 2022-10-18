from pessoa import Pessoa


class Visistante(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: int):
        super().__init__( nome, cpf, telefone)
