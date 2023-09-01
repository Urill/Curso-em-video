import datetime
ficha = dict()
ficha['nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Digite o ano do seu nascimento: '))
ficha['idade'] = datetime.datetime.now().year - nascimento
ficha['carteiratrab'] = int(input('Digite a carteira de trabalho, 0 caso não possuir: '))
if ficha['carteiratrab'] != 0:
    ficha['contrato'] = int(input('Digite o ano de sua contratação: '))
    ficha['salario'] = int(input('Digite seu salário: '))
    sexo = str(input('Digite seu sexo, [F/M]: ')).strip()[0]
    if sexo in 'Mm':
        n = 35
    else:
        n = 30
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['contrato'] + n) - datetime.datetime.now().year)

print(ficha)