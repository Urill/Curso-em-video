def aumentar(preco = 0, taxa = 0):
    resp = preco + (preco * taxa/100)
    return resp

def diminuir(preco = 0, taxa = 0):
    resp = preco - (preco * taxa/100)
    return resp


def dobro(preco = 0):
    resp = preco * 2
    return resp


def metade(preco = 0):
    resp = preco/2
    return resp


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco = 0, taxaa = 10, taxar = 5):
    print('-'*30)
    print('RESUMO OPERAÇÕES'.center(30))
    print('-'*30)
    print(f'Preco analisado: {moeda(preco)}')

