"""

-- FATIAMENTO

# C u r s o   d e   P y  t  h  o  n
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^  ^  ^  ^  ^
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
# a frase tem 15 espaços (incluindo letras e espaços)
# a contagem começa no 0

# print frase "Curso de Python" -> | Output: Curso de Python
# frase[9] ->                      | Output: "P" (Posição 9 é a letra P)
# frase[9:13] ->                   | Output: "Pyth" (sempre um a menos)
# frase[9:13:2] ->                 | Output: "Pxtx" (pula de dois em dois)
# frase[:5] ->                     | Output: se eu omito o inicio, ele começa do zero (o mesmo que 0:5)
# frase[15:] ->                    | Output: se eu omito o final, ele vai ate o fim 
# frase[4::3] ->                   | Output: "0xh" (4:, até o fim -no meio considera 0-, pulando de 3 em 3)

-- ANÁLISE

# len(frase) -> mostra o tamanho da frase (lenght)
# frase.count('o') -> vai contar quantas vezes aparece letra 'o'
# frase.count('o', 0, 13)
# frase.find('pyt')
# frase.find('Android') -> quando nao existe = -1 (-1 = nao encontrado)
# 'Curso' in frase -> false or true

-- TRANSFORMAÇAO

frase.replace('Python', 'Android')
frase.upper() -> transforma tudo em maiusculo
frase.lower() -> transforma tudo em minúsculo
frase.capitalize() -> transforma a 1ª em maiuscula e demais em minusculas
frase.title() -> transforma todas as 1ª em maiusculas e demais em minusculas
frase.strip -> remove espaços excedentes, de inicios e finais de frases (erros de digitação)
frase.rstrip -> remove espaços à direita (erros de digitação)
frase.lstrip -> remove espaços à esquerda (erros de digitação)

-- DIVISAO

frase.split -> divide a frase onde tem espaços (gera uma lista com as palavras)

-- JUNÇAO

'-'.join(frase) -> junta todas as palavras com '-' entre elas 'Curso em video' > curso-em-video

-------------------------

frase = 'Curso em Vídeo'

print(frase)          # Curso em Vídeo
print(frase[9])       # V
print(frase[9:13])    # Víde
print(frase[9:13:2])  # Vd
print(frase[:5])      # Curso
print(frase[9:])      # Vídeo
print(frase[4::3])    # o V

print(len(frase))               # 14
print(frase.count('o'))         # 2
print(frase.count('o', 0, 9))   # 1
print(frase.find('Vídeo'))      # 9
print(frase.find('Android'))    # -1
print('Curso' in frase)         # True
print('Python' in frase)        # False

print(frase.replace('Vídeo', 'Python'))  # Curso em Python
print(frase.upper())                    # CURSO EM VÍDEO
print(frase.lower())                    # curso em vídeo
print(frase.capitalize())               # Curso em vídeo
print(frase.title())                    # Curso Em Vídeo
print(frase.strip())                    # Curso em Vídeo
print(frase.rstrip())                   # Curso em Vídeo
print(frase.lstrip())                   # Curso em Vídeo

frase = '   Curso em Vídeo   '

print(frase.strip())   # 'Curso em Vídeo'
print(frase.rstrip())  # '   Curso em Vídeo'
print(frase.lstrip())  # 'Curso em Vídeo   '

frase = 'Curso em Vídeo'

print('-'.join(frase.split()))  # Curso-em-Vídeo

"""

frase = 'Curso em Vídeo'

print(frase.split())  # ['Curso', 'em', 'Vídeo']