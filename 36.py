import datetime
atual = datetime.date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Você deve se alistar')
elif idade > 18:
    passou = idade - 18
    print('Você deveria ter se alistado há {} '.format(passou))
elif idade < 18:
    tempoaté = 18 - idade
    print('Falta {} anos para vc se alistar'.format(tempoaté))
