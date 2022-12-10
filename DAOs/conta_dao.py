from DAOs.dao import DAO
from models.conta import Conta


class ContaDAO(DAO):
    def __init__(self) -> None:
        super().__init__('contas.pkl')

    def add(self, conta: Conta):
        if conta is not None and isinstance(conta, Conta):
            super().add(conta)

    def update(self, conta: Conta):
        if conta is not None and isinstance(conta, Conta):
            super().update(conta)

    def remove(self, conta: Conta):
        if conta is not None and isinstance(conta, Conta):
            super().remove(conta)
