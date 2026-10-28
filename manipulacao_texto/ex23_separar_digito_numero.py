# ============================================================
# EXERCÍCIO 02 - SEPARANDO DÍGITOS DE UM NÚMERO
# ============================================================

# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separadamente.

# Exemplo:
# Digite um número: 1834

# Saída esperada:
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um número de 0 à 9999: '))

# DESTRINCHANDO O CODIGO:

# numero = (divisor x quociente) + resto

# 1234 / 100   # 12.34      # / divisao comum
# 1234 // 100  # 12         # // divisao inteira

# // retorna o quociente inteiro
# % (módulo) retorna o resto da divisão
# print(1834 // 10)  # 183 → quociente inteiro
# print(1834 % 10)   # 4   → resto da divisão

uni = num // 1 % 10         # divide por 1 > considera SÓ o quociente INTEIRO > % divide por 10 > mostra o resto da divisao %
dez = num // 10 % 10        # divide por 10 > considera SÓ o quociente INTEIRO > % divide por 10 > mostra o resto da divisao %
cen = num // 100 % 10       # divide por 100 > considera SÓ o quociente INTEIRO > % divide por 10 > mostra o resto da divisao %
mil = num // 1000 % 10      # divide por 1000 > considera SÓ o quociente INTEIRO > % divide por 10 > mostra o resto da divisao %

print(f'O número {num} possui: \nUnidade: {uni} \nDezena: {dez} \nCentena: {cen} \nMilhar: {mil}')