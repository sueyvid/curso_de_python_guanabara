s = float(input('Qual o valor do seu salário? '))
if s > 1250:
    aum = s * 0.1
else:
    aum = s * 0.15
ns = s + aum
print('Seu novo salário com aumento de {:.0f}% será de R${:.2f}'.format(aum/s*100, ns))
