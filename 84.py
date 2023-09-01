from random import randint
from operator import itemgetter
jogadas = {'jogador1': randint(1,6), 'jogador2': randint(1,6),'jogador3': randint(1,6),'jogador4': randint(1,6)}
rank = list()
for c, i in jogadas.items():
    print(f'{c} tirou {i} no dado.')
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for c, i in enumerate(rank):
    print(f'O {c+1}o colocado foi o {i[0]} com o numero {i[1]}')
