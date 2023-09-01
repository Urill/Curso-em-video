def ficha(nome = '<desconhecido>' , gols = 0) :
    print (f'O jogador {nome} fez {gols} gols')


nome = str(input('Digite o nome: '))
g = str(input('Digite o número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gols = g)
else:
    ficha(nome, g)

