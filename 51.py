from datetime import date
atual = date.today().year
cont = 0
contN = 0
for c in range(0,7):
    n = int(input('Digite o ano de nascimento: '))
    idade = atual - n
    if idade >= 21:
        cont += 1
    else:
        contN += 1
print('{} já atingiram a maioridade e {} ainda não a atingiram'.format(cont, contN))