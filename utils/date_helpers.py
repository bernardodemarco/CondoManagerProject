def convert_datetime(data) -> str:
    ''' Converte datetime para string compreensível '''
    dia = data.strftime('%d')
    mes = data.strftime('%m')
    ano = data.strftime('%Y')
    hora = data.strftime('%H')
    minuto = data.strftime('%M')
    return f'{dia}/{mes}/{ano} - {hora}:{minuto}'

def convert_date(data) -> str:
    ''' Converte date para string compreensível '''
    dia = data.strftime('%d')
    mes = data.strftime('%m')
    ano = data.strftime('%Y')
    return f'{dia}/{mes}/{ano}'
