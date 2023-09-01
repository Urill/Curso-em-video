soma = 0
maismil = 0
cont = 0
barato = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preco dos produtos: '))
    soma += preco
    cont += 1
    if preco > 1000:
        maismil += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < barato:
            menor = preco
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi{soma}')
print(f'Os produtos que custaram mais de 1000 reais foram: {maismil}')
print(f'O mais barato foi {barato}')
