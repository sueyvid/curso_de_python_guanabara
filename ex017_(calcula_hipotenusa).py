from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = sqrt(co**2 + ca**2)
print('O valor da hipotenusa é igual a {:.2f}'.format(hip))

'''from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('O valor da hipotenusa é igual a {:.2f}'.format(hip))'''
