from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'A contagem de {i} até {f} de {p} em {p}')
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c += p
        print('Fim')
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='',  flush=True)
            sleep (0.5)
            c -= p
        print('Fim')


i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Pulando de: '))
contador(i, f, p)
