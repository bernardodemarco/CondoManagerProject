from DAOs.dao import DAO
from models.tipo_conta import TipoConta


class TipoContaDAO(DAO):
    def __init__(self) -> None:
        super().__init__('tipo_contas.pkl')

    def add(self, tipo_conta: TipoConta):
        if tipo_conta is not None and isinstance(tipo_conta, TipoConta):
            super().add(tipo_conta)

    def update(self, tipo_conta: TipoConta):
        if tipo_conta is not None and isinstance(tipo_conta, TipoConta):
            super().update(tipo_conta)

    def remove(self, tipo_conta: TipoConta):
        if tipo_conta is not None and isinstance(tipo_conta, TipoConta):
            super().remove(tipo_conta)
