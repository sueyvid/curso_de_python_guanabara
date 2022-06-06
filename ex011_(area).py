larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
a = larg * alt
capacidade = 2
# 1 litro de tinta pinta 2m²
tinta = a / capacidade
print('A parede de {}mx{}m tem {}m² de área. \nSerão necessários {:.2f} litros de tinta'.format(larg, alt, a, tinta))
