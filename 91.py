def maior(*num):
    cont = 0
    maior = 0
    for c in num:
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont+=1
    print(f'Foram informados {cont} valores e o maior foi {maior}')

maior(0, 1, 2, 7, 39)



