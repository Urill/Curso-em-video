prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = int(input('Digite a quantidade máxima da pa: '))
c = 0
while c <= n-1 and n != 0:
    rangetotal = prim + n * razao
    c += 1
    print('{}'.format(c))
    #n = int(input('Vc quer mais quantos termos ? '))
