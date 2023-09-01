ficha = dict()
golspartidas = list()
ficha['nome'] = str(input('Digite o nome do jogador: '))
total = int(input(f'Quantas partidas {ficha["nome"]} jogou: '))
for c in range(0, total):
    golspartidas.append(int(input(f'Quantos gols {ficha["nome"]} fez na {c+1}o partida: ')))
ficha['gols'] = golspartidas[:]
ficha['totalgols'] = sum(golspartidas)
print(ficha)
#for c, i in ficha.items():
    #print(f'O {c} tem o valor {i}')
print(f'O jogador {ficha["nome"]} jogou {len(ficha["gols"])} partidas')
for c, v in enumerate(golspartidas):
    print(f'Na {c+1}o partida o {ficha["nome"]} fez {v} gols')
