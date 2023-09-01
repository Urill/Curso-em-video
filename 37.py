n1 = float(input('Digite a p1: '))
n2 = float(input('Digite a p2: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado')
elif media >= 5 and media <=6.9:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')