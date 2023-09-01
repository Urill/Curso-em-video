from datetime import datetime
totpessoas = int(input('Digite quantas pessoas vc quer cadastrar: '))
cont=0
total = list()
pessoa = dict()
soma = media = 0

while cont < totpessoas:
    pessoa.clear()
    cont += 1
    print(f'{cont}o pessoa')
    pessoa['nome'] = str(input('Digite seu nome: '))
    while True:
        pessoa['sexo']= str(input('Digite seu sexo [F/M]: ' )).strip()[0]
        if pessoa['sexo'] not in 'MmFf':
            print('Tente novamente')
            pessoa['sexo']= str(input('Digite seu sexo [F/M]: ' )).strip()[0]
        if pessoa['sexo'] in 'MmFf':
            break
    anonasc = int(input('Digite o ano de nascimento: '))
    pessoa['idade'] = datetime.now().year - anonasc
    soma += pessoa['idade']
    total.append(pessoa.copy())
media = soma/cont
print(f'Foram cadastradas {cont} pessoas')
for c in total:
    if c['sexo'] in 'Ff':
        print(f'As mulheres  cadastradas são {c["nome"]}', end=' ')
print(f'\nA média de idade é {media:.2f} anos')
for c in total:
    if c['idade'] >= media:
        print(f'A pessoa com idade acima da média é {pessoa["nome"]}')
        print('   ')
        '''for k, v in c.items():
            print(f'{k} = {c};', end='')'''
