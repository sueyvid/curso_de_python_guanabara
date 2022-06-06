x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite mais um número: '))
if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
else:
    menor = z
if x > y and x > z:
    maior = x
elif y > x and y > z:
    maior = y
else:
    maior = z

print('O valor maior é {}'.format(maior))
print('O valor menor é {}'.format(menor))
