dados = list()
acesso = list()
maior = menor = 0
while True:
    acesso.append(str(input('Digite seu nome: ')))
    acesso.append(int(input('Digite seu peso: ')))
    if len(dados)==0:
        maior = menor = acesso[1]
    else:
        if acesso[1] > maior:
            maior = acesso[1]
        if acesso[1] < menor:
            menor = acesso[1]
    dados.append(acesso[:])
    acesso.clear()
    op = str(input('Quer continuar ? [S/N]: ')).strip()[0]
    while op not in 'SsNn':
        print('Opção inválida tente novamente')
        op = str(input('Quer continuar ? [S/N]: ')).strip()[0]
    if op in 'Nn':
        break

print(f'As pessoas cadastradas foram {dados}')
print(f'foram cadastradas {len(dados)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in dados:
    if p[1]==maior:
        print({p[0]})
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in dados:
    if p[1]==menor:
        print({p[0]})