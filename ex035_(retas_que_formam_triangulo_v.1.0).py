from math import fabs

x = int(input('Digite um comprimento de reta: '))
y = int(input('Digite outro comprimento de reta: '))
z = int(input('Digite mais um comprimento de reta: '))

if x > y and x > z:
    maior = x
    r2 = y
    r3 = z
elif y > x and y > z:
    maior = y
    r2 = x
    r3 = z
else:
    maior = z
    r2 = x
    r3 = y

if fabs(r2-r3) < maior < r2 + r3:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
