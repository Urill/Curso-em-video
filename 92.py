from random import randint
def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Os nùmeros sorteados são {numeros}')
def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos números pares sorteados é {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)