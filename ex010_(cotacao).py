real = float(input('Digite quanto você tem de dinheiro na carteira: R$'))
c_dolar = 4.88
c_euro = 5.16
c_libra = 6.09
# 1.00 dólar = 3.27 reais
dolar = real/c_dolar
euro = real/c_euro
libra = real/c_libra

print('Você pode comprar: \nUS${:.2f} - dolar \nЄ{:.2f} - euro \n£{:.2f} - libra'.format(dolar, euro, libra))
