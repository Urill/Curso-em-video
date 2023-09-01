valor = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
    else:
        print('Valor já recebido, não irei adicionar')
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while op not in 'SsNn':
        print('Opção inválida')
        op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if op in 'Nn':
        break
valor.sort()
print(valor)