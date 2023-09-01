import random
print('Sua opções: \n[1]Pedra \n[2]Tesoura \n[3]Papel')
p = 'pedra'
t = 'tesoura'
pa = 'papel'
lista = [p, t, pa]
jogador = int(input('Sua opção: '))
computador = random.choice(lista)
if computador == p:
    if jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('computador vence')
    elif jogador == 3:
        print('jogador vence')
    else:
        print('Jogada invalida')
elif computador == t:
    if jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('Empate')
    elif jogador == 3:
        print('Computador vence')
    else:
        print('Jogada invalida')
elif computador == pa:
    if jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Jogador vence')
    elif jogador == 3:
        print('Empate')
    else:
        print('Jogada invalida')
