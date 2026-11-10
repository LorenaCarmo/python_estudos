'''
Programa que lê velocidade de um carro.
Se ultrapassar 80km/hr:
    msg = voce foi multado
A multa custa R$7,00 por km ultrapassado
'''

vel = int(input('A velocidade permitida no Radar é de até 80km/h.\nDigite a velocidade do veículo: '))
multa = ((vel) - 80) * 7

if vel > 80:
    print(f'Você ultrapassou a velocidade permitida. Sua multa é de R${multa:.2f},00.')
else:
    print('Velocidade dentro do limite permitido.')