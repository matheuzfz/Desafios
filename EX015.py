d = int(input('Por quantos dias o carro foi alugado: '))
k = float(input('Qunatos Km foram rodados: '))
vd = (d*60)
vk = (k*0.15)
vt = (vd+vk)
print('O valor total para {}Km e {} dias é {}'.format(k,d,vt))