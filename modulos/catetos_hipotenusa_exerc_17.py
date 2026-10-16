# programa que le o cateto oposto e do cateto adjacente de um triangulo retangulo, 
# calcule e mostre o comprimento da hipotenusa.

# calculo: eleva os dois catetos ao quadrado, soma os resultados e tira a raiz quadrada da soma.
# **(1/2) calcula a raiz quadrada
# **2 eleva um número ao quadrado


from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Agora, digite o valor do cateto adjacente: '))
hi = hypot(co, ca)

print(f'O valor da hipotenusa é: {hi:.2f}')



"""
sem importar math:

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Agora, digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'O valor da hipotenusa é: {hi:.2f}')

"""



