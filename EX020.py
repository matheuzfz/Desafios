import random

n1 = str(input('Insira o primeiro nome: '))
n2 = str(input('Insira o segundo nome: '))
n3 = str(input('Insira o terceiro nome: '))
n4 = str(input('insira o quarto nome: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)
