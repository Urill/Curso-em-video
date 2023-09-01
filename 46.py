n = int(input('Digite o número: '))
n2 = int(input('Digite o número de vezes dá tabuada: '))
for c in range(1, n2+1):
    print('O resultado da tabuada de {} por {} é : {}'.format(n, c, n*c))
