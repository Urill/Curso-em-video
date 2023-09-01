import random
#lista = [0, 1, 2, 3, 4, 5]
#num = random.choice(lista)
n = int(input('Digite um numero de 0 a 5: '))
#if n == num:
#    print('Vc acertou')
#else:
#    print('Tente dnv')
computador = random.randint(0,5)
if n == computador:
    print('Vc ganhou')
else:
    print('Eu ganhei')