from utilidadescv import moeda
from utilidadescv import dado

p = dado.leiaDinheiro('Digite o preco: ')
taxaa = float(input('Digite a taxa: '))
taxar = float(input('Digite a taxa de diminuição: '))
moeda.resumo(p, taxaa, taxar)
