class ResourceNotFoundException(Exception):
    def __init__(self, resource: str) -> None:
        super().__init__(
            f'ERRO!: {resource} não encontrada!')
