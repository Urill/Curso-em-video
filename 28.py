n = float(input('Digite a distância da sua viagem: '))
if n <= 200:
    print('Sua passagem custará {}'.format(n * 0.50))
else:
    print('Sua passagem custará {} '.format(n * 0.45))