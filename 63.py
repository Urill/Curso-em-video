maior = homens = mulheres20 = 0
while True:
    idade = int(input('Coloque a sua idade: '))
    sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Sexo inválido')
        sexo = str(input('Digite seu sexo novamente: ')).strip().upper()[0]
    if idade > 18:
        maior = maior + 1
    if sexo in 'Mm':
        homens = homens + 1
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? ')).strip().upper()[0]
    if resp == 'N':
        break
print(maior)
print(homens)
print(mulheres20)