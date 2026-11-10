'''
todo metodo tem parenteses no final ()

Um método em Python é uma função que está vinculada a um objeto ou a uma classe. Enquanto uma função comum é independente, o método pertence a um objeto e opera diretamente sobre os dados ou comportamentos dele.
'''
# Programa que faz o computador pensar em um numero inteiro de 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. Mostre mensagem dizendo se o usuário acertou ou errou.

tentativa = int(input('Tente adivinhar qual número estou pensando. Digite um número de 1 a 5: '))

if tentativa == 3:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! O número correto era 3!')