n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('{} e {} são iguais'.format(n1, n2))
