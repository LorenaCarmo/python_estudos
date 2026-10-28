"""

----------------------------------
FATIAMENTO
----------------------------------

frase = 'Curso em Vídeo'

print(frase)                            # Curso em Vídeo
print(frase[9])                         # V
print(frase[9:13])                      # Víde
print(frase[9:13:2])                    # Vd
print(frase[:5])                        # Curso
print(frase[9:])                        # Vídeo
print(frase[4::3])                      # o V e

----------------------------------
ANÁLISE
----------------------------------

frase = 'Curso em Vídeo'

print(len(frase))                       # 14        | conta com espaços
print(len(frase.replace(' ', '')))      # 12        | conta sem espaços

print(sum(letra.isalpha() for letra in frase))  # 12

print(frase.count('o'))                 # 2
print(frase.count('o', 0, 9))           # 1
print(frase.find('Vídeo'))              # 9
print(frase.find('Android'))            # -1
print('Curso' in frase)                 # True
print('Python' in frase)                # False

----------------------------------
TRANSFORMAÇAO
----------------------------------

frase = '   Curso em Vídeo   '

print(frase.strip())                    # 'Curso em Vídeo'
print(frase.rstrip())                   # '   Curso em Vídeo'
print(frase.lstrip())                   # 'Curso em Vídeo   '

frase.replace('Python', 'Android')

frase.upper()                           # transforma tudo em maiusculo
frase.lower()                           # transforma tudo em minúsculo
frase.capitalize()                      # transforma a 1ª em maiuscula e demais em minusculas
frase.title()                           # transforma todas as 1ª em maiusculas e demais em minusculas
frase.strip                             # remove espaços excedentes, de inicios e finais de frases (erros de digitação)
frase.rstrip                            # remove espaços à direita (erros de digitação)
frase.lstrip                            # remove espaços à esquerda (erros de digitação)

frase = 'Curso em Vídeo'

print(frase.replace('Vídeo', 'Python')) # Curso em Python
print(frase.upper())                    # CURSO EM VÍDEO
print(frase.lower())                    # curso em vídeo
print(frase.capitalize())               # Curso em vídeo
print(frase.title())                    # Curso Em Vídeo
print(frase.strip())                    # Curso em Vídeo
print(frase.rstrip())                   # Curso em Vídeo
print(frase.lstrip())                   # Curso em Vídeo

----------------------------------
DIVISAO
----------------------------------

frase.split                             # divide a frase onde tem espaços (gera uma lista com as palavras)

frase = '   Curso em Vídeo   '

print(frase.strip())                    # 'Curso em Vídeo'
print(frase.rstrip())                   # '   Curso em Vídeo'
print(frase.lstrip())                   # 'Curso em Vídeo   '

----------------------------------
JUNÇAO
----------------------------------

'-'.join(frase)                         # junta todas as palavras com '-' entre elas 'Curso em video' > curso-em-video


frase = 'Curso em Vídeo'

print('-'.join(frase.split()))          # Curso-em-Vídeo

"""

frase = 'Curso em Vídeo'

print(frase.split())                    # ['Curso', 'em', 'Vídeo']