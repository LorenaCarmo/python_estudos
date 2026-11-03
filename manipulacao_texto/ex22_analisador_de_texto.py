
# ============================================================
# EXERCÍCIO 01 - ANALISANDO UM NOME
# ============================================================

# Crie um programa que leia o nome completo de uma pessoa
# e mostre na tela:

# 1. O nome com todas as letras maiúsculas.
# 2. O nome com todas as letras minúsculas.
# 3. Quantas letras o nome tem ao todo (sem considerar os espaços).
# 4. Quantas letras tem o primeiro nome.

"""
1.
nome = input('Digite seu nome: ')
print(nome.upper())

2.
nome = input('Digite seu nome: ')
print(nome.lower())

3.
nome = input('Digite seu nome: ')
print(len(nome.replace(' ','')))

# 4.
nome = input('Digite seu nome: ')
print(len(nome.split()[0]))
"""

nome = input('Digite seu nome completo: ').strip()

print('Analisando seu nome...')

# nome maiusculas
print(f'Seu nome em letras maiúsculas é: {nome.upper()}.')

# nome minusculas
print(f'Seu nome em letras minúsculas é: {nome.lower()}.')

# qtde de letras
print(f'Seu nome tem ao todo {(len(nome.replace(' ','')))} letras.')

# primeiro nome + qtde letras
# nome.split() → separa o nome em uma lista de palavras.
# nome.split()[0] → retorna 'Lorena'.
# len(nome.split()[0]) → retorna 6.
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem ao todo {len(nome.split()[0])} letras.')