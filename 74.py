valor = list()
cont = 0
while True:
    n = int(input('Digite um valor: '))
    valor.append(n)
    cont += 1
    op = str(input('Vc quer continuar ? [S/N]: ')).strip().upper()[0]
    while op not in 'SN':
        print('Op inválida, digite novamente')
        op = str(input('Vc quer continuar ? [S/N]: ')).strip().upper()[0]
    if op in 'N':
        break
valor.sort(reverse=True)
print(f'A quantidade de números digitados foi {cont}')
print(f'A lista em forma  decrescente é {valor}')
if 5 in valor:
    print('O 5 está presente na lista')
else:
    print('5 não está presente')
