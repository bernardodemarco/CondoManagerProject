import re
from utils.InvalidCPFException import InvalidCPFException


def get_digit(cpf: str, digit: str) -> str:
    ''' Retorna o dígito verificador esperado '''
    ind = 0
    soma = 0
    num = 10 if digit == 'first' else 11

    for i in range(num, 1, -1):
        soma += i * int(cpf[ind])
        ind += 1

    return '0' if (soma * 10 % 11 == 10) else str(soma * 10 % 11)


def validate_cpf(raw_cpf: str):
    ''' Validação do CPF e de seus dígitos verificadores '''
    cpf = raw_cpf.strip()

    if not re.match(r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}-?[0-9]{2}$', cpf):
        raise InvalidCPFException(raw_cpf)

    if not cpf.isdecimal():
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

    if cpf == cpf[0] * 11:
        raise InvalidCPFException(raw_cpf)

    first_digit = get_digit(cpf[:-2], 'first')
    if first_digit != cpf[-2]:
        raise InvalidCPFException(raw_cpf)

    second_digit = get_digit(cpf[:-1], 'second')
    if second_digit != cpf[-1]:
        raise InvalidCPFException(raw_cpf)

    return True
