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
print(frase.count('A'))
print(frase.find('A'))
print(frase.rfind('A'))