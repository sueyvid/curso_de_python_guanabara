dist = float(input('Digite a distânica da viagem em Km: '))
if dist <= 200:
    valor = dist*0.5
else:
    valor = dist*0.45
print('O preço da passagem é: R${:.2f}'.format(valor))
