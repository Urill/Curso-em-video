def fat(num, show=False):
    """
    :param num: Número a ser fatorado
    :param show: True para mostrar a conta se requisitado
    :return: Retornará o resultado do fatorado
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('Digite o número a ser fatorado: '))
op = str(input('Digite True para mostrar a conta: ')).strip().upper()[0]
if op == 'T':
    op = True
else:
    op = False
help(fat)
print(fat(5, op))
