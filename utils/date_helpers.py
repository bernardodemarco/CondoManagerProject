import re

from utils.InvalidTimeException import InvalidTimeException

def convert_datetime(data) -> str:
    ''' Converte datetime para string compreensível '''
    return data.strftime('%d/%m/%Y - %H:%M')

def convert_date(data) -> str:
    ''' Converte date para string compreensível '''
    return data.strftime('%d/%m/%Y')

def validate_horario(horario: str) -> bool:
    ''' 
    Validação de horários na forma hora:minuto,
    horários permitidos -> [(07:00) : (22:00)]
    '''
    if not re.match(r'(([7-9]|0[7-9]|1[0-9]|2[0-1]):[0-5][0-9]|22:00)$', horario):
        raise InvalidTimeException
    return [int(i) for i in horario.split(':')]
