import math
o = float(input('Informe o valor do cateto oposto: '))
a = float(input('Informe o valor do cateto adjacente: '))
print('A hipotenusa desse triângulo é {:.2f}.'.format(math.hypot(o,a)))
