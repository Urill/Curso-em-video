def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):
            print('Erro. Digite um número válido')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError, TypeError):
            print('Erro. Digite um número válido')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida')
            return 0
        else:
            return n


num = leiaint('Digite um valor inteiro: ')
num2 = leiafloat('Digite um valor real: ')
print(f'Você digitou {num}')
print(f'Você digitou {num2}')


