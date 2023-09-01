n = int(input('Digite um numero de 1 a 9999: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print('A unidade, dezena, centena e milhar são: {}, {}, {}, {}'.format(uni, dez, cen, mil))