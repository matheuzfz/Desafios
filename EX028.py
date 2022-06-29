from random import randint
computador = randint(0, 5)
print('*' * 55)
print('Vou pensar em um número entre 0 e 5, Tente adivinhar...')
print('*' * 55)
jogador = int(input('Em qual número você pensou?'))
if computador == jogador:
    print('PARABÉNS, você me venceu!')
else:
    print('Que pena, você errou! Você pensou em {} e eu em {}'.format(jogador,computador))


