'''
Programa que pergunta a distância de uma viagem em km
calcula o preço da passagem cobrando:
R$0,50 por km para viagens até 200km
R$0,45 por km para viagens mais longas que 200km
'''

print('***** Bem vindo(a) ao cobrador de Viagem *****\nVamos calcular o valor da sua passagem.')
viagem = int(input('Digite qual a distância em km da sua viagem: '))

if viagem < 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45

print(f'O valor da sua passagem é de R${valor:.2f}.')

