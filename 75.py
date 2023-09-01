valor = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    valor.append(n)
    op = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    while op not in 'SN':
        print('Op inválida, digite novamente: ')
        op = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if op in 'N':
        break
for c in valor:
    if c % 2 == 0:
        par.append(c)
    elif c % 2 == 1:
        impar.append(c)
print(valor)
print(par)
print(impar)
