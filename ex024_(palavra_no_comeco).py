cidade = str(input('Nome da cidade: ')).strip()
print('Nome da cidade começa com SANTO: {}'.format(cidade.upper().find('SANTO') == 0))
#print('Nome da cidade começa com SANTO: {}'.format(cidade[:5].upper() == 'SANTO'))
