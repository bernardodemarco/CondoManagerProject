class ResourceAlreadyExistsException(Exception):
    def __init__(self, resource: str) -> None:
        super().__init__(
            f'\033[0;31mERRO!: {resource} já existente!\033[1;36m')
