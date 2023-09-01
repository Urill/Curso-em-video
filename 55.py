from random import randint
'''computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou')'''
computador = randint(0, 10)
jogador = int(input('Digite o seu palpite: '))
cont = 1
while jogador != computador or jogador not in (0, 10):
    computador = randint(0, 10)
    jogador = int(input('Tente novamente: '))
    cont += 1
print('Acertou')
print('Vc precisou de {} tentativas'.format(cont))
