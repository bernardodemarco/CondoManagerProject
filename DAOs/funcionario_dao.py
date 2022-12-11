from DAOs.dao import DAO
from models.funcionario import Funcionario


class FuncionarioDAO(DAO):
    def __init__(self) -> None:
        super().__init__('funcionario.pkl')

    def add(self, funcionario: Funcionario):
        if funcionario is not None and isinstance(funcionario, Funcionario):
            super().add(funcionario)

    def update(self, funcionario: Funcionario):
        if funcionario is not None and isinstance(funcionario, Funcionario):
            super().update(funcionario)

    def remove(self, funcionario: Funcionario):
        if funcionario is not None and isinstance(funcionario, Funcionario):
            super().remove(funcionario)
