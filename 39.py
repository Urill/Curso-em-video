r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('As retas não podem formar triângulos')
