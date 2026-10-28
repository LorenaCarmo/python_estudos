# ============================================================
# EXERCÍCIO 06 - PRIMEIRO E ÚLTIMO NOME
# ============================================================

# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

# Exemplo:
# Digite seu nome: Ana Maria de Souza

# Saída esperada:
# Primeiro = Ana
# Último = Souza


'''
Vamos usar aquela forma do -1 como ultima posiçao...
'''

nome = input('Digite seu nome completo: ').strip().title()
separado = nome.split()
print(f'Seu primeiro nome é: {separado[0]}. \nSeu último nome é: {separado[-1]}.')