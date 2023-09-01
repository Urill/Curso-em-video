from datetime import datetime


def voto(i=0):
    idade = datetime.today().year - i
    if 16 < idade < 18 or idade > 65:
        return f'Pessoas com idade {idade} tem direito a voto opcional'
    if 18 <= idade < 65:
        return f'Pessoas com idade de {idade} anos tem dever de voto obrigatório'
    else:
        return 'Não votam'


n = int(input('Digite o ano de seu nascimento: '))
print(voto(n))



