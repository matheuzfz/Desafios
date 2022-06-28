import math
a = float(input('Informe o angulo: '))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('_'*20)
print('Com o angulo de {:.2f}, temos:\nSeno = {:.2f}\nCocesseno = {:.2f}\nTangente = {:.2f}'.format(a,s,c,t))
print('_'*20)
