while True:
    n = int(input('Qual a tabuada q deseja ? '))
    n2 = int(input('Por quantos números vc quer a tabuada? '))
    if n < 0:
        break
    for c in range(1, n2+1):
        print(f'{n} X {c} = {n * c}')
