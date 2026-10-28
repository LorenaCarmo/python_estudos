# ============================================================
# EXERCÍCIO 03 - VERIFICANDO O NOME DE UMA CIDADE
# ============================================================

# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

# Exemplo 1:
# Digite o nome da cidade: Santo André
# Saída esperada: True

# Exemplo 2:
# Digite o nome da cidade: Belo Horizonte
# Saída esperada: False

cidade = input('Digite o nome da sua cidade: ').strip().upper()
print(cidade.startswith('SANTO'))