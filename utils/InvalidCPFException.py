class InvalidCPFException(Exception):
    def __init__(self, cpf: str) -> None:
        super().__init__(f'ERRO!: O CPF {cpf} é inválido!')
