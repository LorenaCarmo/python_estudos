# ============================================================
# EXERCÍCIO 04 - VERIFICANDO SE UM NOME CONTÉM "SILVA"
# ============================================================

# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

# Exemplo 1:
# Digite seu nome: Maria Silva
# Saída esperada: True

# Exemplo 2:
# Digite seu nome: Ana Souza
# Saída esperada: False

nome = input('Digite o seu nome: ').strip().upper()
print('SILVA' in nome)