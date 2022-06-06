print('*'*3 + 'Este é um radar eletrônico' + '*'*3)
v = float(input('Qual é a velocidade do carro? '))
if v > 80:
    print('Você foi multado!')
    multa = (v - 80) * 7
    print('O valor da multa é R${:.2f}'.format(multa))
else:
    print('Nenhum problema! Continue sua viagem.')
