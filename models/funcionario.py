from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: int, inscricao_cnis: int):
        super().__init__(nome, cpf, telefone)
        self.__inscricao_cnis = inscricao_cnis

    @property
    def inscricao_cnis(self):
        return self.__inscricao_cnis
