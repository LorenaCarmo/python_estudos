# leia 4 nomes e sorteie um nome da lista

import random

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print(f'O aluno escolhido foi: {escolhido}')

"""
Outra forma, sem importar toda a random:

from random import choice

n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print(f'O aluno escolhido foi: {escolhido}')

"""