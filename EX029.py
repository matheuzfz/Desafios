vel = float(input('Informe a velocidade do veículo em Km/h: '))
if vel>80:
    print('MULTADO, por exeder o limite da via de 80Km/h.')
    multa = (vel-80)*7
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')

