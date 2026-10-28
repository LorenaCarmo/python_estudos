
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

"""

# 4.
nome = input('Digite seu nome: ')
print(len(nome.split()[0]))