# crie um programa que leia um numero qualquer pelo teclado e mostre o resultado de seu numero inteiro
# .replace(',' , '.') = serve para trocar automaticamente , por .


from math import trunc
num = float(input('Digite um número qualquer: ').replace(',','.'))

print(f'A porção inteira de {num} é: {trunc(num)}')



'''

importando toda a math:

import math
num = float(input('Digite um número qualquer: ').replace(',','.'))
print(f'A porção inteira de {num} é: {math.trunc(num)}')

------

sem importação de math: (nesse caso dá pra fazer sem importar)

num = float(input('Digite um número qualquer: '))
print(f'A porção inteira de {num} é: {int(num)}')

'''