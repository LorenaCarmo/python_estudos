# ============================================================
# EXERCÍCIO 05 - ANALISANDO UMA FRASE
# ============================================================

# Faça um programa que leia uma frase pelo teclado
# e mostre:

# 1. Quantas vezes aparece a letra "A".
# 2. Em que posição ela aparece pela primeira vez.
# 3. Em que posição ela aparece pela última vez.

# Observação:
# Considere letras maiúsculas e minúsculas.

frase = input('Digite uma frase qualquer: ').strip().upper()

print(f'A letra A aparece {frase.count("A")} vezes.')
print(f'A primeira letra A aparece na posição {frase.find("A") + 1}.')
print(f'A última letra A aparece na posição {frase.rfind("A") + 1}.')