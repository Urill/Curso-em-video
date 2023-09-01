n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
'''print('Digite [1] para somar')
print('Digite [2] para multiplicar')
print('Digite [3] para descobrir o maior')
print('Digite [4] para trocar os números')
print('Digite [5] para sair do programa')
op = int(input('Qual a sua opção: '))'''
op = 0
while op != 5:
    print('Digite [1] para somar')
    print('Digite [2] para multiplicar')
    print('Digite [3] para descobrir o maior')
    print('Digite [4] para trocar os números')
    print('Digite [5] para sair do programa')
    op = int(input('Qual a sua opção: '))
    if op == 1:
        soma = n1 + n2
        print('A soma é {}'.format(soma))
    elif op == 2:
        mult = n1 * n2
        print('A mult é {}'.format(mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior é {}'.format(maior))
    elif op == 4:
        n1 = int(input('Digite o novo número: '))
        n2 = int(input('Digite o segundo novo número: '))
    else:
        print('Op inválida')
print('Fim')
