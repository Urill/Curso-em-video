def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro digite um número inteiro')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Vc digitou o número {n}')
