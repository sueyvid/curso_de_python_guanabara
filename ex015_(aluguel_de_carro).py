dias = int(input('Digite quantos dias você passou com o carro: '))
km = float(input('Digite por quantos km você rodou com o carro: '))
total = dias * 60
total += 0.15 * km
print('O valor a ser pago é: R${:.2f}'.format(total))
