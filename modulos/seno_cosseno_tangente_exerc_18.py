# programa que lê um angulo qualquer e mostra na tela:
# seu seno, seu coseno e sua tangente

import math

angulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} é {seno:.2f}.')

cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {cosseno} é {cosseno:.2f}.')

tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {tangente} é {tangente:.2f}.')

"""
Outra forma:

import math

angulo = float(input('Digite o ângulo: '))
rad = math.radians(angulo)

print(f'Seno: {math.sin(rad):.2f}')
print(f'Cosseno: {math.cos(rad):.2f}')
print(f'Tangente: {math.tan(rad):.2f}')

"""
