n = int(input('Digite um num: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[30m', end='')
    print('{} '.format(c), end='')