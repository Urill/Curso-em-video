s = 0
cont = 0
quant = 0
soma = 0
for c in range(0,6):
    n = int(input('Digite o número: '))
    quant = quant + 1
    soma = soma + n
    if n % 2 == 0:
        s += n
    else:
        cont = cont + 1
print('A contagem de impares é : {}'.format(cont))
print('A soma dos pares dos números digitados é : {} '.format(s))
print('A quantidade de números digitados foi {}.'.format(quant))
print('A soma de todos os números é : {}'.format(soma))