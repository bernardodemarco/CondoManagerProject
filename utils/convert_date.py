def convert_date(data):
    dia = data.strftime('%d')
    mes = data.strftime('%m')
    ano = data.strftime('%Y')
    hora = data.strftime('%H')
    minuto = data.strftime('%M')
    return f'{dia}/{mes}/{ano} - {hora}:{minuto}'
