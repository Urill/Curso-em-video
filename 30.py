n1 = float(input('Digite o primeiro número '))
n2 = float(input('Digite o segundo número '))
n3 = float(input('Digite o terceiro número '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n1:
    menor = n2
print('O menor valor é {}'.format(menor))
maior = n3
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
print('O maior valor é {}'.format(maior))