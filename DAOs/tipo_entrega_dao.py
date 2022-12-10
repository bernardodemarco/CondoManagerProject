from DAOs.dao import DAO
from models.entrega import TipoEntrega


class TipoEntregaDAO(DAO):
    def __init__(self) -> None:
        super().__init__('tipo_entregas.pkl')

    def add(self, tipo_entrega: TipoEntrega):
        if tipo_entrega is not None and isinstance(tipo_entrega, TipoEntrega):
            super().add(tipo_entrega)

    def update(self, tipo_entrega: TipoEntrega):
        if tipo_entrega is not None and isinstance(tipo_entrega, TipoEntrega):
            super().update(tipo_entrega)

    def remove(self, tipo_entrega: TipoEntrega):
        if tipo_entrega is not None and isinstance(tipo_entrega, TipoEntrega):
            super().remove(tipo_entrega)
