from datetime import date
atual = date.today().year
anonasc = int(input('Digite o ano de nascimento: '))
idade = atual - anonasc
if idade <= 9:
    print('Categoria mirim')
elif 9 < idade <= 14 :
    print('Categoria infantil')
elif 14 < idade <= 19 :
    print('Categoria junior')
elif idade == 20 :
    print('Categoria Sênior')
elif idade > 20 :
    print('Categoria Master')