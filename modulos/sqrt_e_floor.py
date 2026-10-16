# exercicio para importar apenas raiz quadrada (sqrt) do modulo math
# e também já arredonda para baixo (floor)
# importando o floor já facilita no codigo

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é: {raiz}')