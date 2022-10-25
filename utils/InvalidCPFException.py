class InvalidCPFException(Exception):
    def __init__(self, cpf: str) -> None:
        super().__init__(f'\033[0;31mERRO!: O CPF {cpf} é inválido!\033[1;36m')
