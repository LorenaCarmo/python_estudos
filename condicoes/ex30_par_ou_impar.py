'''
Programa que lê um numero
Analise se é par ou se é impar
Mostra a msg na tela com o resultado da analise
'''

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print('Este é um número par.')
else:
    print('Este é um número ímpar.')