from math import sin, cos, tan, pi
ang = float(input('Digite um ângulo: '))
# ang*pi = 180*x
ang *= pi/180
sen = sin(ang)
cos = cos(ang)
tan = tan(ang)
print('sen = {:.2f} \ncos = {:.2f} \ntan = {:.2f}'.format(sen, cos, tan))
